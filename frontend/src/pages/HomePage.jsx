import Footer from "../components/Footer";
import Navbar from "../components/Navbar";
import RoomCard from "../components/RoomCard";
import ServiceCard from "../components/ServiceCard";
import BookingWidget from "../components/BookingWidget";
import LocationCard from "../components/LocationCard";
import { 
  Star, 
  Utensils, 
  Dumbbell, 
  Wifi, 
  Car, 
  Coffee,
  Sparkles,
  Award,
  Shield,
  Clock
} from "lucide-react";

export default function App() {
  const rooms = [
    {
      name: "Phòng Deluxe",
      description: "Phòng sang trọng với đầy đủ tiện nghi hiện đại, view thành phố tuyệt đẹp",
      price: "1.500.000đ / đêm",
      image: "https://images.unsplash.com/photo-1670800050441-e77f8c82963f?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxob3RlbCUyMGRlbHV4ZSUyMHJvb218ZW58MXx8fHwxNzY0MTA4NjU1fDA&ixlib=rb-4.1.0&q=80&w=1080",
      capacity: "2 người",
      size: "35m²"
    },
    {
      name: "Suite Cao Cấp",
      description: "Suite rộng rãi với phòng khách riêng, view panorama và ban công riêng",
      price: "2.800.000đ / đêm",
      image: "https://images.unsplash.com/photo-1725962479542-1be0a6b0d444?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxob3RlbCUyMHN1aXRlJTIwYmVkcm9vbXxlbnwxfHx8fDE3NjQwOTgxNDd8MA&ixlib=rb-4.1.0&q=80&w=1080",
      capacity: "3 người",
      size: "60m²"
    },
    {
      name: "Presidential Suite",
      description: "Phòng tổng thống đẳng cấp 5 sao với không gian sống xa hoa",
      price: "5.000.000đ / đêm",
      image: "https://images.unsplash.com/photo-1748652252546-6bea5d896bd4?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxob3RlbCUyMHByZXNpZGVudGlhbCUyMHN1aXRlfGVufDF8fHx8MTc2NDA5NjUyM3ww&ixlib=rb-4.1.0&q=80&w=1080",
      capacity: "4 người",
      size: "120m²"
    }
  ];

  const featuredRooms = [
    {
      name: "Phòng Deluxe",
      description: "Phòng sang trọng với đầy đủ tiện nghi hiện đại, view thành phố tuyệt đẹp",
      price: "1.500.000đ / đêm",
      image: "https://images.unsplash.com/photo-1670800050441-e77f8c82963f?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxob3RlbCUyMGRlbHV4ZSUyMHJvb218ZW58MXx8fHwxNzY0MTA4NjU1fDA&ixlib=rb-4.1.0&q=80&w=1080",
      capacity: "2 người",
      size: "35m²",
      featured: true
    },
    {
      name: "Suite Cao Cấp",
      description: "Suite rộng rãi với phòng khách riêng, view panorama và ban công riêng",
      price: "2.800.000đ / đêm",
      image: "https://images.unsplash.com/photo-1725962479542-1be0a6b0d444?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxob3RlbCUyMHN1aXRlJTIwYmVkcm9vbXxlbnwxfHx8fDE3NjQwOTgxNDd8MA&ixlib=rb-4.1.0&q=80&w=1080",
      capacity: "3 người",
      size: "60m²",
      featured: true
    }
  ];

  const services = [
    {
      title: "Nhà Hàng Cao Cấp",
      description: "Thưởng thức ẩm thực đa dạng từ Á đến Âu do đầu bếp 5 sao chế biến",
      icon: Utensils,
      image: "https://images.unsplash.com/photo-1640108930193-76941e385e5e?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxob3RlbCUyMHJlc3RhdXJhbnQlMjBkaW5pbmd8ZW58MXx8fHwxNzY0MDcxNzUxfDA&ixlib=rb-4.1.0&q=80&w=1080"
    },
    {
      title: "Spa & Wellness",
      description: "Thư giãn và tái tạo năng lượng với dịch vụ spa chuyên nghiệp",
      icon: Sparkles,
      image: "https://images.unsplash.com/photo-1604161926875-bb58f9a0d81b?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxob3RlbCUyMHNwYSUyMHdlbGxuZXNzfGVufDF8fHx8MTc2NDEzNzQxNnww&ixlib=rb-4.1.0&q=80&w=1080"
    },
    {
      title: "Phòng Gym",
      description: "Phòng tập gym hiện đại với đầy đủ thiết bị cho mọi nhu cầu tập luyện",
      icon: Dumbbell
    },
    {
      title: "WiFi Tốc Độ Cao",
      description: "Kết nối internet miễn phí với tốc độ cao trong toàn bộ khách sạn",
      icon: Wifi
    },
    {
      title: "Dịch Vụ Đưa Đón",
      description: "Xe đưa đón sân bay và tour du lịch theo yêu cầu",
      icon: Car
    },
    {
      title: "Quán Cafe 24/7",
      description: "Thưởng thức cà phê và đồ uống bất cứ lúc nào trong ngày",
      icon: Coffee
    }
  ];

  const nearbyLocations = [
    {
      name: "Sân bay Tân Sơn Nhất",
      type: "Sân bay quốc tế",
      distance: "8 km (15 phút lái xe)"
    },
    {
      name: "Nhà thờ Đức Bà",
      type: "Di tích lịch sử",
      distance: "2 km (5 phút lái xe)"
    },
    {
      name: "Bến Thành Market",
      type: "Chợ truyền thống",
      distance: "1.5 km (10 phút đi bộ)"
    },
    {
      name: "Phố đi bộ Nguyễn Huệ",
      type: "Khu vui chơi giải trí",
      distance: "2.5 km (7 phút lái xe)"
    },
    {
      name: "Thảo Cầm Viên Sài Gòn",
      type: "Công viên động vật",
      distance: "3 km (10 phút lái xe)"
    },
    {
      name: "Bitexco Financial Tower",
      type: "Trung tâm thương mại",
      distance: "3.5 km (12 phút lái xe)"
    }
  ];

  const testimonials = [
    {
      name: "Nguyễn Minh Anh",
      rating: 5,
      comment: "Khách sạn tuyệt vời! Phòng ốc sạch sẽ, nhân viên thân thiện. Sẽ quay lại lần sau.",
      date: "20/11/2023"
    },
    {
      name: "Trần Văn Nam",
      rating: 5,
      comment: "Vị trí thuận tiện, view đẹp, đồ ăn ngon. Đáng giá từng đồng bỏ ra!",
      date: "15/11/2023"
    },
    {
      name: "Lê Thị Hương",
      rating: 5,
      comment: "Trải nghiệm tuyệt vời! Dịch vụ chuyên nghiệp, không gian sang trọng.",
      date: "10/11/2023"
    }
  ];

  return (
    <div className="min-h-screen flex flex-col">
      <Navbar />
      
      <section className="relative h-[600px] flex items-center justify-center">
        <div className="absolute inset-0">
          <img
            src="https://images.unsplash.com/photo-1723465308831-29da05e011f3?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxsdXh1cnklMjBob3RlbCUyMGV4dGVyaW9yfGVufDF8fHx8MTc2NDExNzMwOHww&ixlib=rb-4.1.0&q=80&w=1080"
            alt="Lotus Hotel"
            className="w-full h-full object-cover"
          />
          <div className="absolute inset-0 bg-black/40"></div>
        </div>
        
        <div className="relative z-10 text-center text-white space-y-6 px-4">
          <h1 className="text-5xl md:text-6xl font-bold">Chào mừng đến Lotus Hotel</h1>
          <p className="text-xl md:text-2xl max-w-3xl mx-auto">
            Trải nghiệm kỳ nghỉ đẳng cấp 5 sao với dịch vụ hoàn hảo và không gian sang trọng
          </p>
          <div className="flex gap-4 justify-center flex-wrap">
            <button className="bg-green-700 hover:bg-green-800 text-white px-6 py-3 rounded-md text-lg font-medium transition-colors duration-200">
              Đặt phòng ngay
            </button>
            <button className="bg-white/90 hover:bg-white text-gray-900 px-6 py-3 rounded-md text-lg font-medium border border-transparent hover:border-gray-300 transition-colors duration-200">
              Khám phá thêm
            </button>
          </div>
        </div>
      </section>

      <section className="py-8 bg-gray-50 -mt-16 relative z-20">
        <div className="max-w-7xl mx-auto px-4">
          <BookingWidget />
        </div>
      </section>

      <section className="py-20 bg-white">
        <div className="max-w-7xl mx-auto px-4">
          <div className="text-center mb-12">
            <h2 className="mb-4 text-3xl font-bold text-gray-800">Phòng nổi bật</h2>
            <p className="text-xl text-gray-600 max-w-2xl mx-auto">
              Những lựa chọn phòng được yêu thích nhất tại Lotus Hotel
            </p>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-5xl mx-auto">
            {featuredRooms.map((room, index) => (
              <RoomCard key={index} {...room} />
            ))}
          </div>
        </div>
      </section>

      <section id="about" className="py-20 bg-gray-50">
        <div className="max-w-7xl mx-auto px-4">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
            <div>
              <h2 className="mb-6 text-3xl font-bold text-gray-800">Giới thiệu Lotus Hotel</h2>
              <p className="text-lg text-gray-600 mb-6">
                Lotus Hotel là khách sạn 5 sao đẳng cấp quốc tế tọa lạc tại trung tâm thành phố, 
                mang đến trải nghiệm nghỉ dưỡng sang trọng và đẳng cấp cho mọi du khách.
              </p>
              <p className="text-lg text-gray-600 mb-6">
                Với hơn 200 phòng và suite được thiết kế tinh tế, đội ngũ nhân viên chuyên nghiệp, 
                và các tiện nghi hiện đại, chúng tôi cam kết mang đến những khoảnh khắc nghỉ ngơi 
                tuyệt vời nhất cho quý khách.
              </p>
              <div className="grid grid-cols-3 gap-6 mt-8">
                <div className="text-center">
                  <div className="w-16 h-16 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-3">
                    <Award className="h-8 w-8 text-green-700" />
                  </div>
                  <p className="text-sm text-gray-600">Giải thưởng<br/>5 sao</p>
                </div>
                <div className="text-center">
                  <div className="w-16 h-16 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-3">
                    <Shield className="h-8 w-8 text-green-700" />
                  </div>
                  <p className="text-sm text-gray-600">An toàn<br/>& Tin cậy</p>
                </div>
                <div className="text-center">
                  <div className="w-16 h-16 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-3">
                    <Clock className="h-8 w-8 text-green-700" />
                  </div>
                  <p className="text-sm text-gray-600">Phục vụ<br/>24/7</p>
                </div>
              </div>
            </div>
            <div className="relative h-[500px] rounded-lg overflow-hidden shadow-xl">
              <img
                src="https://images.unsplash.com/photo-1723465308831-29da05e011f3?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxsdXh1cnklMjBob3RlbCUyMGV4dGVyaW9yfGVufDF8fHx8MTc2NDExNzMwOHww&ixlib=rb-4.1.0&q=80&w=1080"
                alt="Lotus Hotel Building"
                className="w-full h-full object-cover"
              />
            </div>
          </div>
        </div>
      </section>

      <section className="py-20 bg-white">
        <div className="max-w-7xl mx-auto px-4">
          <div className="text-center mb-12">
            <h2 className="mb-4 text-3xl font-bold text-gray-800">Địa điểm gần khách sạn</h2>
            <p className="text-xl text-gray-600 max-w-2xl mx-auto">
              Khám phá các điểm đến hấp dẫn xung quanh Lotus Hotel
            </p>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {nearbyLocations.map((location, index) => (
              <LocationCard key={index} {...location} />
            ))}
          </div>
        </div>
      </section>

      <section id="rooms" className="py-20 bg-gray-50">
        <div className="max-w-7xl mx-auto px-4">
          <div className="text-center mb-12">
            <h2 className="mb-4 text-3xl font-bold text-gray-800">Tất cả Phòng & Suite</h2>
            <p className="text-xl text-gray-600 max-w-2xl mx-auto">
              Lựa chọn phòng phù hợp với nhu cầu của bạn
            </p>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {rooms.map((room, index) => (
              <RoomCard key={index} {...room} />
            ))}
          </div>
        </div>
      </section>

      <section id="services" className="py-20 bg-gray-50">
        <div className="max-w-7xl mx-auto px-4">
          <div className="text-center mb-12">
            <h2 className="mb-4 text-3xl font-bold text-gray-800">Dịch vụ tiện ích</h2>
            <p className="text-xl text-gray-600 max-w-2xl mx-auto">
              Trải nghiệm đầy đủ các tiện ích cao cấp tại khách sạn
            </p>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {services.map((service, index) => (
              <ServiceCard key={index} {...service} />
            ))}
          </div>
        </div>
      </section>

      <section className="py-20 bg-white">
        <div className="max-w-7xl mx-auto px-4">
          <div className="text-center mb-12">
            <h2 className="mb-4 text-3xl font-bold text-gray-800">Đánh giá từ khách hàng</h2>
            <p className="text-xl text-gray-600 max-w-2xl mx-auto">
              Những chia sẻ từ khách hàng đã trải nghiệm dịch vụ của chúng tôi
            </p>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {testimonials.map((testimonial, index) => (
              <div key={index} className="bg-white p-6 rounded-lg border shadow-sm hover:shadow-md transition-shadow">
                <div className="flex items-center gap-1 mb-4">
                  {[...Array(testimonial.rating)].map((_, i) => (
                    <Star key={i} className="h-5 w-5 fill-yellow-400 text-yellow-400" />
                  ))}
                </div>
                <p className="text-gray-600 mb-4">{testimonial.comment}</p>
                <div className="border-t pt-4">
                  <p className="font-medium text-gray-800">{testimonial.name}</p>
                  <p className="text-sm text-gray-500">{testimonial.date}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      <section id="contact" className="py-20 bg-green-700 text-white">
        <div className="max-w-4xl mx-auto px-4 text-center space-y-6">
          <h2 className="text-3xl font-bold">Sẵn sàng đặt phòng?</h2>
          <p className="text-xl text-white/90">
            Liên hệ với chúng tôi ngay hôm nay để được tư vấn và đặt phòng với giá tốt nhất
          </p>
          <div className="flex gap-4 justify-center flex-wrap">
            <button className="bg-white text-green-700 hover:bg-gray-100 px-6 py-3 rounded-md text-lg font-medium transition-colors duration-200">
              Gọi ngay: 1900-xxxx
            </button>
            <button className="border-2 border-white text-white hover:bg-white/10 px-6 py-3 rounded-md text-lg font-medium transition-colors duration-200">
              Email: info@lotushotel.vn
            </button>
          </div>
        </div>
      </section>
      
      <Footer />
    </div>
  );
}