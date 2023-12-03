import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from pathlib import Path
load_dotenv()



class Config(BaseSettings):
    APP_NAME: str = os.environ.get('APP_NAME', "Web Scrapping")
    DEBUG: bool = bool(os.environ.get('DEBUG', False))


class LocalConfig(Config):
    # Database Variable
    DB_HOST: str = os.environ.get('DB_HOST')
    DB_PORT: str = os.environ.get('DB_PORT')
    DB_USERNAME: str = os.environ.get('DB_USER')
    DB_PASSWORD: str = os.environ.get('DB_PASSWORD')
    DB_URL: str = f'postgresql+asyncpg://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/web_scraps'


def get_config():
    env = os.environ.get('ENV', 'local')
    config_type = {
        'local': LocalConfig()
    }
    return config_type[env]


config = get_config()
