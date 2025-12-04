import React, { useState } from 'react'
import { Menu, X, Calendar, User } from "lucide-react";

const Navbar = () => {
    const [isMenuOpen, setIsMenuOpen] = useState(false);

  const menuItems = [
    { name: "Trang chủ", href: "#" },
    { name: "Phòng", href: "#rooms" },
    { name: "Dịch vụ", href: "#services" },
    { name: "Giới thiệu", href: "#about" },
    { name: "Liên hệ", href: "#contact" },
  ];

  return (
    <nav className="bg-white border-b border-gray-200 sticky top-0 z-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">
          <div className="shrink-0">
            <h1 className="text-2xl font-bold text-green-700">Lotus Hotel</h1>
          </div>

          <div className="hidden md:block">
            <div className="ml-10 flex items-baseline space-x-8">
              {menuItems.map((item) => (
                <a
                  key={item.name}
                  href={item.href}
                  className="text-gray-700 hover:text-green-700 px-3 py-2 rounded-md transition-colors duration-200"
                >
                  {item.name}
                </a>
              ))}
            </div>
          </div>

          <div className="hidden md:flex items-center space-x-4">
            <button className="flex items-center gap-2 text-gray-700 hover:text-green-700 px-3 py-2 rounded-md transition-colors duration-200">
              <Calendar className="h-5 w-5" />
              Đặt phòng
            </button>
            <button className="flex items-center gap-2 text-gray-700 hover:text-green-700 px-3 py-2 rounded-md transition-colors duration-200">
              <User className="h-5 w-5" />
              Đăng nhập
            </button>
            <button className="bg-green-700 hover:bg-green-800 text-white px-4 py-2 rounded-md transition-colors duration-200">
              Đăng ký
            </button>
          </div>

          <div className="md:hidden">
            <button
              onClick={() => setIsMenuOpen(!isMenuOpen)}
              className="text-gray-700 p-2 rounded-md hover:bg-gray-100 transition-colors duration-200"
            >
              {isMenuOpen ? (
                <X className="h-6 w-6" />
              ) : (
                <Menu className="h-6 w-6" />
              )}
            </button>
          </div>
        </div>

        {isMenuOpen && (
          <div className="md:hidden">
            <div className="px-2 pt-2 pb-3 space-y-1 sm:px-3 border-t border-gray-200">
              {menuItems.map((item) => (
                <a
                  key={item.name}
                  href={item.href}
                  className="text-gray-700 hover:text-green-700 block px-3 py-2 rounded-md transition-colors duration-200"
                  onClick={() => setIsMenuOpen(false)}
                >
                  {item.name}
                </a>
              ))}
              <div className="pt-4 pb-2 space-y-2">
                <button className="flex items-center w-full text-left text-gray-700 hover:text-green-700 px-3 py-2 rounded-md transition-colors duration-200">
                  <Calendar className="h-5 w-5 mr-2" />
                  Đặt phòng
                </button>
                <button className="flex items-center w-full text-left text-gray-700 hover:text-green-700 px-3 py-2 rounded-md transition-colors duration-200">
                  <User className="h-5 w-5 mr-2" />
                  Đăng nhập
                </button>
                <button className="w-full bg-green-700 hover:bg-green-800 text-white px-3 py-2 rounded-md transition-colors duration-200">
                  Đăng ký
                </button>
              </div>
            </div>
          </div>
        )}
      </div>
    </nav>
  );
}

export default Navbar