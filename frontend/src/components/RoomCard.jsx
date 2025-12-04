import React from 'react'
import { Users, Maximize2, Wifi } from "lucide-react";

const RoomCard = ({ name, description, price, image, capacity, size }) => {
    return (
    <div className="bg-white rounded-lg overflow-hidden shadow-lg hover:shadow-xl transition-shadow duration-300">
      <div className="relative h-64 overflow-hidden">
        <img
          src={image}
          alt={name}
          className="w-full h-full object-cover hover:scale-110 transition-transform duration-300"
        />
        <div className="absolute top-4 right-4 bg-green-700 text-white px-4 py-2 rounded-lg font-medium">
          {price}
        </div>
      </div>
      
      <div className="p-6">
        <h3 className="mb-2 text-xl font-bold text-gray-800">{name}</h3>
        <p className="text-gray-600 mb-4">{description}</p>
        
        <div className="flex items-center gap-4 mb-4 text-sm text-gray-500">
          <div className="flex items-center gap-1">
            <Users className="h-4 w-4" />
            <span>{capacity}</span>
          </div>
          <div className="flex items-center gap-1">
            <Maximize2 className="h-4 w-4" />
            <span>{size}</span>
          </div>
          <div className="flex items-center gap-1">
            <Wifi className="h-4 w-4" />
            <span>WiFi miễn phí</span>
          </div>
        </div>
        
        <button className="w-full bg-green-700 hover:bg-green-800 text-white py-3 rounded-md font-medium transition-colors duration-200">
          Đặt phòng ngay
        </button>
      </div>
    </div>
  );
}

export default RoomCard