from fastapi import FastAPI
from src.books.routes import books_router
from contextlib import asynccontextmanager
from src.db.main import init_db
from src.auth.routes import auth_router


@asynccontextmanager
async def life_span(app: FastAPI):
    print(f"Server is starting up...")

    await init_db()

    yield

    print(f"Server is shutting down...")


version = "v1"
app = FastAPI(
    title="Bookly API",
    description="A simple API for managing books",
    version=version,
)

app.include_router(books_router, prefix=f"/api/{version}/books", tags=["books"])
app.include_router(auth_router, prefix=f"/api/{version}/auth", tags=["auth"])
