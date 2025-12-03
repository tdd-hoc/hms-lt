from fastapi import BackgroundTasks
from typing import List

class EmailService:
    def __init__(self):
        # Ở đây bạn có thể cấu hình SMTP server thực tế
        pass

    def send_email_background(self, background_tasks: BackgroundTasks, email_to: str, subject: str, body: str):
        """
        Hàm wrapper để đẩy việc gửi mail vào nền (background)
        """
        background_tasks.add_task(self._mock_send_email, email_to, subject, body)

    def _mock_send_email(self, email_to: str, subject: str, body: str):
        """
        Hàm giả lập gửi email (In ra console thay vì gửi thật)
        """
        print(f"--------------------------------------------------")
        print(f"📧 [MOCK EMAIL] Sending to: {email_to}")
        print(f"📝 Subject: {subject}")
        print(f"📄 Body: {body}")
        print(f"✅ Status: Sent")
        print(f"--------------------------------------------------")

    # --- Các mẫu email cụ thể ---

    def send_welcome_email(self, background_tasks: BackgroundTasks, email_to: str, name: str):
        subject = "Welcome to Our Hotel!"
        body = f"Hello {name},\n\nThank you for registering an account with us. We hope you have a pleasant stay!"
        self.send_email_background(background_tasks, email_to, subject, body)

    def send_booking_confirmation(self, background_tasks: BackgroundTasks, email_to: str, booking_id: int, room_number: str):
        subject = f"Booking Confirmation #{booking_id}"
        body = f"Your booking for Room {room_number} has been confirmed. See you soon!"
        self.send_email_background(background_tasks, email_to, subject, body)

# Tạo một instance để dùng chung
email_service = EmailService()