from fastapi import FastAPI

from config import config

app = FastAPI()


@app.on_event("startup")
async def startup():
    print(config)
