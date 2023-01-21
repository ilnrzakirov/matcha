
LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "console": {
            "format": "%(asctime)s | %(levelname)s | %(module)s | %(lineno)s | %(message)s",
        },
        "file": {
            "format": "%(asctime)s | [%(levelname)s] | %(name)s | %(module)s|%(lineno)s | %(message)s",
        },
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "formatter": "console",
            "stream": "ext://sys.stdout",
            "class": "logging.StreamHandler",
        },
        "file": {
            "level": "INFO",
            "formatter": "file",
            "class": "logging.FileHandler",
            "filename": "log.log",
            "mode": "a",
        },
    },
    "loggers": {
        "console": {
            "handlers": ["console", "file"],
            "level": "INFO",
        },
        "file": {
            "handlers": ["file"],
            "level": "INFO",
        },
    },
}
