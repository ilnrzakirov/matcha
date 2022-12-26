import uvicorn

from logger.config import LOGGING_CONFIG
from main import app

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="",
        port=9098,
        log_config=LOGGING_CONFIG
    )