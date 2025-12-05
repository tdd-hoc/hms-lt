import axios from 'axios';

// Tạo một instance của Axios với cấu hình mặc định
const axiosClient = axios.create({
    // baseURL: 'http://localhost:8000/api/v1', <--- Cũ (Local)
    baseURL: 'https://hms-longtime-d6bhapazfye9g6fx.eastasia-01.azurewebsites.net/api/v1', // <--- Mới (Azure) // Đường dẫn gốc tới Backend FastAPI của bạn
    headers: {
        'Content-Type': 'application/json',
    },
});

// --- Interceptors (Bộ đón chặn) ---

// 1. Trước khi gửi request: Tự động đính kèm Token (nếu đã đăng nhập)
axiosClient.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem('access_token');
        if (token) {
            config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
);

// 2. Sau khi nhận response: Xử lý lỗi chung (VD: Token hết hạn -> Tự logout)
axiosClient.interceptors.response.use(
    (response) => {
        return response.data; // Trả về dữ liệu sạch
    },
    (error) => {
        // Nếu lỗi 401 (Unauthorized), có thể xử lý logout tại đây
        if (error.response && error.response.status === 401) {
            // localStorage.removeItem('access_token');
            // window.location.href = '/login';
        }
        return Promise.reject(error);
    }
);

export default axiosClient;