from pydantic import BaseModel, Field

class BookCreate(BaseModel):
    title: str
    author: str
    published_year: int
    isbn: str

class BookResponse(BookCreate):
    id: int

    class Config:
        from_attributes = True