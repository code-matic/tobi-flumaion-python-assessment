import logging
import sys

def setup_logger(name: str = __name__, level: int = logging.INFO) -> logging.Logger:
    """
    Sets up a logger with a specified name and logging level.
    
    This logger writes to the console with a standard format.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(level)
        
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        console_handler.setFormatter(formatter)
        
        logger.addHandler(console_handler)
    
    return logger
