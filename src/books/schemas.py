from pydantic import BaseModel


class Book (BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: str
    pagecount: int
    language: str

class BookUpdateModel (BaseModel):
    title: str
    author: str
    publisher: str
    pagecount: int
    language: str