from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse
import pandas as pd
from typing import List, Optional
import os

from .models import Book # Importa o modelo Pydantic

# --- Configuração Inicial da Aplicação ---

# Define a descrição que aparecerá no Swagger/OpenAPI
description = """
API para extração de dados de livros do site 'books.toscrape.com'. 🚀

Você pode:
* **Listar todos os livros**
* **Obter detalhes de um livro específico por ID**
* **Buscar livros por título e/ou categoria**
* **Listar todas as categorias disponíveis**
"""

app = FastAPI(
    title="BookScraper API",
    description=description,
    version="1.0.0",
    contact={
        "name": "Marcelo",
        "email": "email@example.com",
    },
)

# --- Carregamento dos Dados ---

# O caminho para o arquivo CSV
DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'books.csv')

# Carrega os dados do CSV para um DataFrame do Pandas na inicialização da API
try:
    df_books = pd.read_csv(DATA_PATH)
    # Adiciona uma coluna 'id' baseada no índice do DataFrame
    df_books.reset_index(inplace=True)
    df_books.rename(columns={'index': 'id'}, inplace=True)
except FileNotFoundError:
    print(f"ERRO: O arquivo de dados '{DATA_PATH}' não foi encontrado. Execute o script de scraping primeiro.")
    # Se o arquivo não existir, cria um DataFrame vazio para evitar que a API quebre na inicialização
    df_books = pd.DataFrame()


# --- Endpoints da API ---

@app.get("/api/v1/health", tags=["Status"])
async def health_check():
    """
    Verifica o status da API.
    Retorna um status 'ok' se a API estiver funcionando e os dados estiverem carregados.
    """
    if not df_books.empty:
        return JSONResponse(content={"status": "ok", "data_loaded": True, "books_count": len(df_books)})
    else:
        return JSONResponse(content={"status": "error", "data_loaded": False, "message": "Dados não encontrados."}, status_code=503)

@app.get("/api/v1/categories", tags=["Livros"], response_model=List[str])
async def get_categories():
    """
    Lista todas as categorias de livros disponíveis na base de dados.
    """
    if df_books.empty:
        raise HTTPException(status_code=503, detail="Os dados dos livros não estão disponíveis.")
    
    categories = df_books['category'].unique().tolist()
    return categories

@app.get("/api/v1/books", tags=["Livros"], response_model=List[Book])
async def get_all_books():
    """
    Lista todos os livros disponíveis na base de dados.
    """
    if df_books.empty:
        raise HTTPException(status_code=503, detail="Os dados dos livros não estão disponíveis.")
    
    # Converte o DataFrame para uma lista de dicionários e retorna
    return df_books.to_dict(orient='records')

@app.get("/api/v1/books/search", tags=["Livros"], response_model=List[Book])
async def search_books(
    title: Optional[str] = Query(None, min_length=3, description="Busca livros por parte do título."),
    category: Optional[str] = Query(None, description="Filtra livros por uma categoria específica.")
):
    """
    Busca livros por título e/ou categoria.
    Pelo menos um dos parâmetros (title ou category) deve ser fornecido.
    """
    if not title and not category:
        raise HTTPException(status_code=400, detail="Forneça um 'title' ou 'category' para a busca.")

    result_df = df_books.copy()

    if title:
        # Filtra por título (case-insensitive)
        result_df = result_df[result_df['title'].str.contains(title, case=False, na=False)]

    if category:
        # Filtra por categoria (case-insensitive)
        result_df = result_df[result_df['category'].str.lower() == category.lower()]
    
    if result_df.empty:
        raise HTTPException(status_code=404, detail="Nenhum livro encontrado com os critérios fornecidos.")

    return result_df.to_dict(orient='records')


@app.get("/api/v1/books/{book_id}", tags=["Livros"], response_model=Book)
async def get_book_by_id(book_id: int):
    """
    Retorna os detalhes completos de um livro específico pelo seu ID.
    O ID corresponde ao índice do livro no arquivo CSV (começando em 0).
    """
    if df_books.empty:
        raise HTTPException(status_code=503, detail="Os dados dos livros não estão disponíveis.")

    if book_id < 0 or book_id >= len(df_books):
        raise HTTPException(status_code=404, detail=f"Livro com ID {book_id} não encontrado.")
    
    book = df_books.loc[book_id].to_dict()
    return book


