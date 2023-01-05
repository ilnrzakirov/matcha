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


class Configuration(BaseSettings):
    postgres: PostgresSettings
    uvicorn: UvicornSettings
    jwt: JWTSettings

    class Config:
        env_file = ".env",
        env_nested_delimiter = "__"


config = Configuration()
