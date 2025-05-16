import logging
from logging.handlers import RotatingFileHandler
from shared.settings import Settings

settings = Settings()

# Configure root logger
logger = logging.getLogger()
logger.setLevel(settings.LOG_LEVEL)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(settings.LOG_LEVEL)
console_handler.setFormatter(formatter)

# File handler
file_handler = RotatingFileHandler(settings.LOG_FILE, maxBytes=5*1024*1024, backupCount=3)
file_handler.setLevel(settings.LOG_LEVEL)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)
