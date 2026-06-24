from datetime import timedelta, datetime, timezone
import jwt
from passlib.context import CryptContext
from src.config import Config
import uuid
import logging

password_context = CryptContext(schemes=["bcrypt"])

ACCESS_TOKEN_EXPIRY = 3600


def generate_password_hash(password: str) -> str:
    hash = password_context.hash(password)
    return hash


def verify_password(password: str, hash: str) -> bool:
    return password_context.verify(password, hash)


def create_access_token(
    user_data: dict, expiry: timedelta = None, refresh: bool = False
):
    payload = {}
    payload["user"] = user_data
    expire = (
        datetime.now(timezone.utc) + expiry
        if expiry is not None
        else datetime.now(timezone.utc) + timedelta(seconds=ACCESS_TOKEN_EXPIRY)
    )

    payload["exp"] = expire
    payload["jti"] = str(uuid.uuid4())
    payload["refresh"] = refresh

    token = jwt.encode(
        payload=payload, key=Config.JWT_SECRET_KEY, algorithm=Config.JWT_ALGORITHM
    )
    return token


def decode_access_token(token: str) -> dict:
    try:
        token_data = jwt.decode(
            jwt=token, key=Config.JWT_SECRET_KEY, algorithms=[Config.JWT_ALGORITHM]
        )
        return token_data
    except jwt.PYJWTError as e:
        logging.exception(e)
        return None
