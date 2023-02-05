from pydantic import (
    BaseModel,
    BaseSettings,
)


class PostgresSettings(BaseModel):
    host: str
    port: int
    database: str
    password: str
    user: str


class UvicornSettings(BaseModel):
    host: str
    port: int


class JWTSettings(BaseModel):
    key: str


class UserManager(BaseModel):
    key: str


class Configuration(BaseSettings):
    """
        Пайдантик класс для переменных окружения
    """
    postgres: PostgresSettings
    uvicorn: UvicornSettings
    jwt: JWTSettings
    user_manager: UserManager

    class Config:
        env_file = ".env",
        env_nested_delimiter = "__"


config = Configuration()
