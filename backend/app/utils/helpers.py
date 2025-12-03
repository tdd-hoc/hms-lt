import random
import string
from datetime import datetime

def generate_transaction_id(prefix: str = "TRX") -> str:
    """
    Sinh mã giao dịch ngẫu nhiên. VD: TRX-20231025-A1B2C
    """
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    random_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    return f"{prefix}-{timestamp}-{random_str}"

def generate_booking_ref() -> str:
    """
    Sinh mã đặt phòng ngắn gọn. VD: BK-9X8Y7
    """
    random_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return f"BK-{random_str}"