import React, { useState } from 'react'
import { Calendar, Users, Bed, DollarSign } from "lucide-react";

const BookingWidget = () => {
  const [checkIn, setCheckIn] = useState("");
  const [checkOut, setCheckOut] = useState("");
  const [roomType, setRoomType] = useState("");
  const [priceRange, setPriceRange] = useState("");
  const [guests, setGuests] = useState("2");

  const handleSubmit = (e) => {
    e.preventDefault();
    alert("Đang tìm kiếm phòng phù hợp...");
  };

  const roomTypes = [
    { value: "all", label: "Tất cả" },
    { value: "deluxe", label: "Phòng Deluxe" },
    { value: "suite", label: "Suite Cao Cấp" },
    { value: "presidential", label: "Presidential Suite" }
  ];

  const priceRanges = [
    { value: "all", label: "Tất cả" },
    { value: "budget", label: "Dưới 1.5 triệu" },
    { value: "mid", label: "1.5 - 3 triệu" },
    { value: "luxury", label: "Trên 3 triệu" }
  ];

  return (
    <div className="bg-white rounded-lg shadow-2xl p-6 md:p-8 max-w-6xl mx-auto">
      <h2 className="mb-6 text-center text-2xl font-bold text-gray-800">Tìm phòng phù hợp</h2>
      
      <form onSubmit={handleSubmit} className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-6 gap-4">
        <div className="space-y-2 lg:col-span-1">
          <label htmlFor="check-in" className="flex items-center gap-2 text-sm font-medium text-gray-700">
            <Calendar className="h-4 w-4 text-green-700" />
            Ngày nhận phòng
          </label>
          <input
            id="check-in"
            type="date"
            value={checkIn}
            onChange={(e) => setCheckIn(e.target.value)}
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500 focus:border-transparent"
            required
          />
        </div>

        <div className="space-y-2 lg:col-span-1">
          <label htmlFor="check-out" className="flex items-center gap-2 text-sm font-medium text-gray-700">
            <Calendar className="h-4 w-4 text-green-700" />
            Ngày trả phòng
          </label>
          <input
            id="check-out"
            type="date"
            value={checkOut}
            onChange={(e) => setCheckOut(e.target.value)}
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500 focus:border-transparent"
            required
          />
        </div>

        <div className="space-y-2 lg:col-span-1">
          <label htmlFor="room-type" className="flex items-center gap-2 text-sm font-medium text-gray-700">
            <Bed className="h-4 w-4 text-green-700" />
            Loại phòng
          </label>
          <select
            id="room-type"
            value={roomType}
            onChange={(e) => setRoomType(e.target.value)}
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500 focus:border-transparent"
          >
            <option value="">Chọn loại phòng</option>
            {roomTypes.map((type) => (
              <option key={type.value} value={type.value}>{type.label}</option>
            ))}
          </select>
        </div>

        <div className="space-y-2 lg:col-span-1">
          <label htmlFor="price-range" className="flex items-center gap-2 text-sm font-medium text-gray-700">
            <DollarSign className="h-4 w-4 text-green-700" />
            Mức giá
          </label>
          <select
            id="price-range"
            value={priceRange}
            onChange={(e) => setPriceRange(e.target.value)}
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500 focus:border-transparent"
          >
            <option value="">Chọn mức giá</option>
            {priceRanges.map((price) => (
              <option key={price.value} value={price.value}>{price.label}</option>
            ))}
          </select>
        </div>

        <div className="space-y-2 lg:col-span-1">
          <label htmlFor="guests" className="flex items-center gap-2 text-sm font-medium text-gray-700">
            <Users className="h-4 w-4 text-green-700" />
            Số khách
          </label>
          <input
            id="guests"
            type="number"
            min="1"
            max="10"
            value={guests}
            onChange={(e) => setGuests(e.target.value)}
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500 focus:border-transparent"
            required
          />
        </div>

        <div className="flex items-end lg:col-span-1">
          <button 
            type="submit" 
            className="w-full bg-green-700 hover:bg-green-800 text-white py-2 px-4 rounded-md transition-colors duration-200 h-10"
          >
            Tìm phòng
          </button>
        </div>
      </form>
    </div>
  );
}

export default BookingWidget