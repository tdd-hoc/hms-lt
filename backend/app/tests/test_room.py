def test_create_room(client):
    response = client.post(
        "/api/v1/rooms/",
        json={
            "Room_Number": "101",
            "Room_Type": "Deluxe",
            "Base_Price": 500000,
            "Status": "Available",
            "Image_URLs": ["img1.jpg", "img2.jpg"]
        },
    )
    assert response.status_code == 201
    data = response.json()
    assert data["Room_Number"] == "101"
    
    # --- SỬA DÒNG DƯỚI ĐÂY ---
    # Cách 1: So sánh string (Khuyên dùng với Decimal)
    # API trả về "500000.00" (2 số thập phân do MySQL DECIMAL(12,2))
    assert float(data["Base_Price"]) == 500000.0 
    
    # Hoặc nếu bạn muốn so sánh chính xác string:
    # assert data["Base_Price"] == "500000.00"

def test_read_rooms(client):
    response = client.get("/api/v1/rooms/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0 # Vì đã tạo 1 phòng ở trên
    assert data[0]["Room_Number"] == "101"