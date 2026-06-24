from unittest import result
import uuid
from sqlmodel import select, desc
from sqlmodel.ext.asyncio.session import AsyncSession
from datetime import datetime
from src.books.models import Book
from .schemas import BookCreateModel, BookUpdateModel


class BookService:
    async def get_all_books(self, session: AsyncSession):
        statement = select(Book).order_by(desc(Book.created_at))
        result = await session.exec(statement)
        return result.all()

    async def get_book(self, book_uid: uuid.UUID, session: AsyncSession):
        statement = select(Book).where(Book.uid == book_uid)
        result = await session.exec(statement)
        book = result.first()
        return book if book is not None else None

    async def create_book(self, book_data: BookCreateModel, session: AsyncSession):
        new_book = Book(**book_data.model_dump())
        session.add(new_book)
        await session.commit()
        await session.refresh(new_book)
        return new_book

    async def update_book(
        self, book_uid: uuid.UUID, update_data: BookUpdateModel, session: AsyncSession
    ):
        book_to_update = await self.get_book(book_uid, session)

        if book_to_update is not None:
            update_data_dict = update_data.model_dump()
            for k, v in update_data_dict.items():
                setattr(book_to_update, k, v)

            await session.commit()
            return book_to_update
        else:
            return None

    async def delete_book(self, book_uid: uuid.UUID, session: AsyncSession):

        book_to_delete = await self.get_book(book_uid, session)
        if book_to_delete is not None:
            await session.delete(book_to_delete)
            await session.commit()
            return {}
        else:
            return None
