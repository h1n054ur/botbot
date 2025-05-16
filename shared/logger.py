"""Utility module for getting module-level loggers."""
import logging

def get_logger(name: str) -> logging.Logger:
    """Get a module-level logger with the given name."""
    return logging.getLogger(name)