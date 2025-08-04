import logging

def setup_logger(name=__name__):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Avoid duplicate handlers if logger is re-imported
    if not logger.handlers:
        # Console handler
        stream_handler = logging.StreamHandler()
        stream_formatter = logging.Formatter("[%(asctime)s] %(levelname)s - %(message)s")
        stream_handler.setFormatter(stream_formatter)
        logger.addHandler(stream_handler)

        # File handler
        file_handler = logging.FileHandler("app.log")
        file_formatter = logging.Formatter("[%(asctime)s] %(levelname)s - %(message)s")
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

    return logger

logger = setup_logger()
