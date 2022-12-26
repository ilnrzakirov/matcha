from pydantic import (
    BaseModel,
    BaseSettings,
)


class PostgresSettings(BaseModel):
    host: str
    port: str
    database: str
    password: str
    user: str


class UvicornSettings(BaseModel):
    host: str
    port: str


class Configuration(BaseSettings):
    postgres: PostgresSettings
    uvicorn: UvicornSettings

    class Config:
        env_file = ".env",
        env_nested_delimiter = "__"


config = Configuration()
