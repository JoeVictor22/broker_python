import logging
from logging.config import dictConfig


def log_config():
    dictConfig(
        {
            "version": 1,
            "formatters": {
                "default": {
                    "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
                }
            },
            "root": {"level": "INFO"},
        }
    )
    logger = logging.Logger(name="server")
    return logger
