import os
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from dotenv import load_dotenv
from typing import Annotated, AsyncIterator
from fastapi import Depends
from sqlalchemy.exc import SQLAlchemyError


load_dotenv()


db_user_name = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')

DatabaseURL = f'postgresql+asyncpg://{db_user_name}:{db_password}@{db_host}:{db_port}/web_scraps'

async_engine = create_async_engine(url=DatabaseURL, echo=True)
async_session_local = async_sessionmaker(
    bind=async_engine,
    autoflush=False,
    expire_on_commit=False
)


async def get_session() -> AsyncIterator[async_sessionmaker]:
    try:
        yield async_session_local
    except SQLAlchemyError as e:
        print(e)

AsyncSession = Annotated[async_sessionmaker, Depends(get_session)]


# class Base(DeclarativeBase):
#     pass
