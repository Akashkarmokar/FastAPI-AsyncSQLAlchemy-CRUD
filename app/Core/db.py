import os
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase
from dotenv import load_dotenv


load_dotenv()


db_user_name = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')

DatabaseURL = f'postgresql+asyncpg://{db_user_name}:{db_password}@{db_host}:{db_port}/web_scraps'

async_engine = create_async_engine(url=DatabaseURL, echo=True)


class Base(DeclarativeBase):
    pass
