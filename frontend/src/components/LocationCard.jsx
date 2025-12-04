import React from 'react'
import { MapPin } from "lucide-react";

const LocationCard = ({ name, distance, type }) => {
  return (
    <div className="flex items-start gap-4 p-4 bg-white rounded-lg border hover:shadow-md transition-shadow">
      <div className="w-12 h-12 bg-green-100 rounded-full flex items-center justify-center shrink-0">
        <MapPin className="h-6 w-6 text-green-700" />
      </div>
      <div className="flex-1">
        <h4 className="mb-1">{name}</h4>
        <p className="text-sm text-muted-foreground">{type}</p>
        <p className="text-sm text-green-700 mt-1">{distance}</p>
      </div>
    </div>
  );
}

export default LocationCard