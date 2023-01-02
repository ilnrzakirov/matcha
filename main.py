import logging

from fastapi import FastAPI

app = FastAPI()


@app.on_event("startup")
async def startup():
    console_log = logging.getLogger("console")
    console_log.info("Сервис запущен")
