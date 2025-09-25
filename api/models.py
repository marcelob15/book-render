from pydantic import BaseModel

class Book(BaseModel):
    """
    Modelo Pydantic que representa um livro.
    Este modelo é usado para validação de dados e para gerar o esquema da API (Swagger).
    """
    id: int
    title: str
    price: str  # Mantido como string para preservar o símbolo da moeda, ex: £51.77
    rating: int
    availability: int
    category: str
    image_url: str
    book_url: str

    class Config:
        # Permite que o modelo seja criado a partir de objetos ORM ou dicionários
        from_attributes = True
        #orm_mode = True