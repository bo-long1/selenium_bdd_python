import logging
import logging.config

LOG_FILE = "app.log"

logging_config = {
    "version": 1,
    "formatters": {
        "detailed": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        }
    },
    "handlers": {
        "file": {
            "class": "logging.FileHandler",
            "filename": LOG_FILE,
            "formatter": "detailed",
            "level": "DEBUG",
            "encoding": "utf-8"  # Thêm encoding UTF-8
        },
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "detailed",
            "level": "INFO"
        }
    },
    "root": {
        "handlers": ["file", "console"],
        "level": "DEBUG"
    }
}

logging.config.dictConfig(logging_config)
logger = logging.getLogger("AutomationTest")
