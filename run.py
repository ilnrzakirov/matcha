import uvicorn

from logger.config import LOGGING_CONFIG
from main import app
from config import config

if __name__ == "__main__":
    uvicorn.run(
        app,
        host=config.uvicorn.host,
        port=config.uvicorn.port,
        log_config=LOGGING_CONFIG
    )