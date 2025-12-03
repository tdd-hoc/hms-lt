import logging
import sys

# Cấu hình Logger
# Giúp in ra log có định dạng: [TIME] [LEVEL] Message
def setup_logger(name: str = "app"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Nếu đã có handler rồi thì không add thêm (tránh bị log 2 lần)
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            fmt="%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    
    return logger

# Khởi tạo instance để dùng luôn
logger = setup_logger()