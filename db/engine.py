from typing import AsyncGenerator

import databases
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
)
from sqlalchemy.ext.declarative import (
    DeclarativeMeta,
    declarative_base,
)
from sqlalchemy.orm import sessionmaker

from config import config

URL = f"postgresql+asyncpg://{config.postgres.user}:{config.postgres.password}@" \
      f"{config.postgres.host}:{config.postgres.port}/{config.postgres.database}"

database = databases.Database(URL)

engine = create_async_engine(URL)

Base: DeclarativeMeta = declarative_base()

async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
