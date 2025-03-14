from sqlalchemy import create_engine
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    dev_mode: bool = False
    app_host: str
    app_port: int
    db_name: str
    db_user: str
    db_password: str
    db_host: str
    db_port: int

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'


DB_CONNECTION = f'mysql+pymysql://{Settings().db_user}:{Settings().db_password}@{Settings().db_host}:{Settings().db_port}/{Settings().db_name}'

engine = create_engine(DB_CONNECTION, echo=Settings().dev_mode)

