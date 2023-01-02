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


class Configuration(BaseSettings):
    postgres: PostgresSettings
    uvicorn: UvicornSettings

    class Config:
        env_file = ".env",
        env_nested_delimiter = "__"


config = Configuration()
