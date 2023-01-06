import logging

from fastapi import FastAPI
from fastapi_users import FastAPIUsers

from auth.auth import auth_backend
from db.models.user import User
from repository.user import get_user_manager
from repository.user_schemas import (
    UserCreate,
    UserRead,
)

app = FastAPI()

console_log = logging.getLogger("console")

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)


@app.on_event("startup")
async def startup():
    console_log.info("Сервис запущен")


@app.on_event("shutdown")
async def shutdown():
    console_log.info("Сервис остановлен")


app.include_router(
    fastapi_users.get_auth_router(backend=auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
