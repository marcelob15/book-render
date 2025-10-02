# book-render
book-render


'''
### **3. Executando a API Localmente**

Com os arquivos `api/models.py` e `api/main.py` prontos, agora podemos rodar nossa API.

1.  Abra seu terminal na pasta raiz do projeto (`book-api`).
2.  Execute o seguinte comando para iniciar o servidor:
    ```bash
    uvicorn api.main:app --reload
    uvicorn api.main:app --reload --port 9000
    
    externo 
    uvicorn api.main:app --reload --host 0.0.0.0 --port 9000
    ```
    *   `uvicorn`: É o servidor ASGI que vai "rodar" nossa aplicação FastAPI.
    *   `api.main:app`: Indica ao Uvicorn para encontrar o objeto `app` dentro do arquivo `api/main.py`.
    *   `--reload`: Faz com que o servidor reinicie automaticamente sempre que você salvar uma alteração no código.

3.  Se tudo estiver certo, você verá uma saída parecida com esta:
    ```
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    INFO:     Started reloader process [xxxxx]
    INFO:     Started server process [xxxxx]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    ```

### **4. Testando a API e a Documentação (Swagger)**

O FastAPI gera automaticamente uma documentação interativa da sua API.

1.  Abra seu navegador e acesse: **http://127.0.0.1:8000/docs**
                                   http://127.0.0.1:9000/docs

Você verá a interface do Swagger UI, onde pode ver todos os seus endpoints, seus modelos de dados e até mesmo testá-los diretamente pelo navegador!



**Teste alguns endpoints:**

*   Clique no endpoint `GET /api/v1/health`, depois em "Try it out" e "Execute". Você verá o status da API.
*   Tente o `GET /api/v1/categories` para ver a lista de categorias.
*   Tente o `GET /api/v1/books/{book_id}`. Coloque `5` no campo `book_id` e execute.
*   Experimente a busca em `GET /api/v1/books/search`, fornecendo um `title` como "light".

'''


Pos Tech - Fase 1 - Curso de Machine Leanring Engineering
Nome: MB
RM: 368902


# BookScrape API: O Ponto de Partida para Recomendações de Livros Inteligentes

**Transforme dados brutos da web em informações valiosas e práticas com uma API robusta, escalável e pronta para uso.
A BookScrape API é a solução completa para alimentar seus modelos de Machine Learning e sistemas de 
recomendação com dados de livros.**

[![Status da API](https://img.shields.io/website?url=LINK_DO_SEU_DEPLOY/api/v1/health)](LINK_DO_SEU_DEPLOY/docs)
[![Linguagem](https://img.shields.io/badge/Python-3.9-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Framework-FastAPI-green.svg)](https://fastapi.tiangolo.com/)

---

## 🚀 Links Rápidos

*   **API em Produção:** [LINK_DO_SEU_DEPLOY/docs](LINK_DO_SEU_DEPLOY/docs)
*   **Vídeo de Apresentação:** [LINK_DO_VÍDEO_NO_YOUTUBE_OU_SIMILAR](LINK_DO_VÍDEO_NO_YOUTUBE_OU_SIMILAR)

---

## 📖 Visão Geral do Projeto

"A BookScrape API foi desenvolvida para solucionar a necessidade de um dataset de livros estruturado para aplicações de Machine Learning. 
O projeto automatiza o ciclo de extração e transformação dos dados, disponibilizando-os através de uma interface RESTful para o desenvolvimento de modelos de recomendação e outras análises."

Por que funciona:

"Solucionar a necessidade": É uma forma objetiva de apresentar o propósito do projeto.
"Automatiza o ciclo de extração e transformação": Descreve a função técnica principal de forma sucinta.
"Interface RESTful": Termo técnico preciso para descrever a API.
"Simplificar e acelerar o desenvolvimento": Foca nos benefícios práticos para o desenvolvedor/cientista.


### Arquitetura do Sistema

A arquitetura foi projetada para ser simples, eficiente e escalável, garantindo que os dados fluam 
de forma amigável desde a fonte até o consumidor final (seja ele um Cientista de Dados, um notebook de análise ou outra aplicação).

![Diagrama da Arquitetura](LINK_PARA_IMAGEM_DO_SEU_DIAGRAMA)



O fluxo de trabalho é dividido em três etapas principais:
1.  **Ingestão de Dados:** Um script de Web Scraping robusto navega pelo site [books.toscrape.com](http://books.toscrape.com), extraindo informações detalhadas de cada livro.
2.  **Armazenamento:** Os dados coletados são limpos, estruturados e armazenados em um formato CSV, criando uma base de dados local, leve e portátil.
3.  **Disponibilização (API):** Uma API RESTful, construída com FastAPI, lê os dados processados e os expõe através de endpoints, permitindo consultas.


---

## ⚙️ Como Reproduzir o Projeto Localmente

Siga os passos abaixo para ter o ambiente completo rodando na sua máquina.

### Pré-requisitos

*   Python 3.9+
*   Pip (gerenciador de pacotes)

### Instalação

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
    cd SEU_REPOSITORIO
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

### Execução

1.  **Execute o Web Scraper (Opcional):**
    Para gerar um novo arquivo `books.csv`, execute o scraper. Os dados já estão inclusos no repositório.
    ```bash
    python scripts/scraper.py
    ```

2.  **Inicie a API:**
    A API será servida localmente em `http://127.0.0.1:8000`.
    ```bash
    uvicorn api.main:app --reload
    ```
	Caso queria rodar em outra porta coloque --port 9000 no final
	uvicorn api.main:app --reload --port 9000
	
	

3.  **Acesse a documentação interativa (Swagger):**
    Abra o seu navegador e acesse [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

---

## 📚 Documentação da API

A seguir, estão os endpoints disponíveis para consulta.

### `GET /api/v1/health`

Verifica a saúde da API. Ideal para monitoramento e health checks.

*   **Exemplo de Resposta (200 OK):**
    ```json
    {
      "status": "ok",
      "message": "API is running and data is available."
    }
    ```

### `GET /api/v1/categories`

Retorna uma lista com todas as categorias de livros disponíveis.

*   **Exemplo de Resposta (200 OK):**
    ```json
    {
      "categories": [
        "Travel",
        "Mystery",
        "Historical Fiction",
        ...
      ]
    }
    ```

### `GET /api/v1/books`

Lista todos os livros da base de dados com suporte a paginação.

*   **Parâmetros de Query:**
    *   `skip` (int, opcional): Número de registros a pular. Default: 0.
    *   `limit` (int, opcional): Número máximo de registros a retornar. Default: 10.

*   **Exemplo de Chamada:** `LINK_DO_SEU_DEPLOY/api/v1/books?skip=0&limit=5`
*   **Exemplo de Resposta (200 OK):**
    ```json
    [
      {
        "id": 1,
        "title": "A Light in the Attic",
        "price": "£51.77",
        "rating": 3,
        "availability": "In stock",
        "category": "Poetry",
        "image_url": "http://books.toscrape.com/media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg"
      },
      ...
    ]
    ```

### `GET /api/v1/books/{id}`

Retorna os detalhes completos de um livro específico pelo seu ID.

*   **Exemplo de Chamada:** `LINK_DO_SEU_DEPLOY/api/v1/books/1`
*   **Exemplo de Resposta (200 OK):**
    ```json
    {
      "id": 1,
      "title": "A Light in the Attic",
      "price": "£51.77",
      "rating": 3,
      "availability": "In stock",
      "category": "Poetry",
      "image_url": "http://books.toscrape.com/media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg"
    }
    ```

### `GET /api/v1/books/search`

Busca livros por título e/ou categoria. Os filtros são combinados (operação "E").

*   **Parâmetros de Query:**
    *   `title` (str, opcional): Parte do título do livro a ser buscado (case-insensitive).
    *   `category` (str, opcional): Categoria exata do livro.

*   **Exemplo de Chamada:** `LINK_DO_SEU_DEPLOY/api/v1/books/search?title=light&category=Poetry`
*   **Exemplo de Resposta (200 OK):**
    ```json
    [
        {
            "id": 1,
            "title": "A Light in the Attic",
            "price": "£51.77",
            "rating": 3,
            "availability": "In stock",
            "category": "Poetry",
            "image_url": "http://books.toscrape.com/media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg"
        }
    ]
    ```

---
