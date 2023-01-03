import logging

from fastapi import FastAPI

app = FastAPI()

console_log = logging.getLogger("console")


@app.on_event("startup")
async def startup():
    console_log.info("Сервис запущен")


@app.on_event("shutdown")
async def shutdown():
    console_log.info("Сервис остановлен")
