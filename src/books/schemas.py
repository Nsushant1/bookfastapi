import uuid
from datetime import date, datetime
from pydantic import BaseModel


class Book(BaseModel):
    uid: uuid.UUID
    title: str
    author: str
    publisher: str
    published_date: date
    pagecount: int
    language: str
    created_at: datetime
    updated_at: datetime


class BookCreateModel(BaseModel):
    title: str
    author: str
    publisher: str
    published_date: date
    pagecount: int
    language: str


class BookUpdateModel(BaseModel):
    title: str | None = None
    author: str | None = None
    publisher: str | None = None
    published_date: date | None = None
    pagecount: int | None = None
    language: str | None = None
