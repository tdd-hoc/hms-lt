def test_register_customer(client):
    response = client.post(
        "/api/v1/customers/register",
        json={
            "Name": "Test User",
            "Email": "test@example.com",
            "Password": "password123",
            "Phone_Number": "0987654321"
        },
    )
    assert response.status_code == 201
    data = response.json()
    assert data["Email"] == "test@example.com"
    assert "Customer_ID" in data

def test_login_customer(client):
    # Đăng nhập bằng tài khoản vừa tạo
    response = client.post(
        "/api/v1/customers/login",
        data={ # Login dùng form-data, không phải json
            "username": "test@example.com",
            "password": "password123"
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_register_duplicate_email(client):
    # Thử đăng ký lại email cũ
    response = client.post(
        "/api/v1/customers/register",
        json={
            "Name": "Test User 2",
            "Email": "test@example.com", # Trùng
            "Password": "password123"
        },
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Email already registered"