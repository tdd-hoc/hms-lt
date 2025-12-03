from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import date
from decimal import Decimal

from app.models.payment import Payment, PaymentStatus
from app.models.booking import Booking, BookingStatus
from app.models.room import Room, RoomStatus

class ReportService:
    
    # 1. Tính tổng doanh thu theo khoảng thời gian
    def get_revenue_report(self, db: Session, start_date: date, end_date: date) -> Decimal:
        """
        Tổng tiền từ các giao dịch thanh toán thành công (Paid) trong khoảng thời gian.
        """
        total_revenue = db.query(func.sum(Payment.Amount)).filter(
            Payment.Status == PaymentStatus.Paid,
            func.date(Payment.Payment_Date) >= start_date,
            func.date(Payment.Payment_Date) <= end_date
        ).scalar()
        
        return total_revenue or Decimal(0.0)

    # 2. Tính tỷ lệ lấp đầy phòng (Occupancy Rate) hiện tại
    def get_occupancy_rate(self, db: Session) -> float:
        """
        Tỷ lệ % = (Số phòng đang có khách / Tổng số phòng) * 100
        """
        total_rooms = db.query(func.count(Room.Room_ID)).scalar()
        if total_rooms == 0:
            return 0.0
        
        # Đếm số phòng đang Booked hoặc Cleaning (coi như không trống)
        occupied_rooms = db.query(func.count(Room.Room_ID)).filter(
            Room.Status.in_([RoomStatus.Booked, RoomStatus.Cleaning])
        ).scalar()
        
        rate = (occupied_rooms / total_rooms) * 100
        return round(rate, 2)

    # 3. Đếm số lượng Booking theo trạng thái (Thống kê Dashboard)
    def get_booking_stats(self, db: Session):
        """
        Trả về: {'Reserved': 5, 'Confirmed': 10, 'Cancelled': 2...}
        """
        results = db.query(Booking.Status, func.count(Booking.Booking_ID)).group_by(Booking.Status).all()
        # Chuyển list tuple thành dict
        stats = {status.value: count for status, count in results}
        return stats

report_service = ReportService()