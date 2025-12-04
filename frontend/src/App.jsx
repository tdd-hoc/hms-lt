import {react} from "react"
import HomePage from "../src/pages/HomePage"
import LoginPage from "./pages/LoginPage"
import Dashboard from "./pages/Dashboard"
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';


function App() {

  return (

    <Router>
      <Routes>
        {/* Đường dẫn mặc định chuyển hướng sang Login */}
        <Route path="/" element={<HomePage/>} />
        
        {/* Định nghĩa các trang */}
        <Route path="/login" element={<LoginPage />} />
        <Route path="/dashboard" element={<Dashboard />} />
        
        {/* Trang 404 (nếu nhập linh tinh) */}
        <Route path="*" element={<div className="p-10">404 - Page Not Found</div>} />
      </Routes>
    </Router>
  )
}

export default App
