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


class Configuration(BaseSettings):
    postgres: PostgresSettings

    class Config:
        env_file = ".env",
        env_nested_delimiter = "__"

config = Configuration()
