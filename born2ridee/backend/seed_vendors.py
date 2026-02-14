import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'born2ride.settings')
django.setup()

from core_api.models import Vendor

def seed_data():
    # Clear existing vendors to avoid duplicates and ensure a fresh set of fake data
    Vendor.objects.all().delete()
    
    vendors = [
        # Hotels from different sources
        {
            'name': 'The Grand Residency',
            'vendor_type': 'hotel',
            'description': 'Luxury stay with premium amenities and city view.',
            'address': 'Trichy Main Road, Perambalur',
            'latitude': 11.2341,
            'longitude': 78.8789,
            'rating': 4.8,
            'phone': '9876543210',
            'price_range': '₹₹₹',
            'timing': '24 Hours',
            'rooms_available': 5,
            'base_price': 3500.00,
            'source': 'goibibo'
        },
        {
            'name': 'Highway Inn',
            'vendor_type': 'hotel',
            'description': 'Comfortable rooms for travelers. Budget friendly.',
            'address': 'Chennai Bypass, Trichy',
            'latitude': 10.8050,
            'longitude': 78.6856,
            'rating': 4.2,
            'phone': '9876543211',
            'price_range': '₹₹',
            'timing': '24 Hours',
            'rooms_available': 12,
            'base_price': 1500.00,
            'source': 'mmt'
        },
        {
            'name': 'Skyline Hotel',
            'vendor_type': 'hotel',
            'description': 'Modern hotel with great food and parking.',
            'address': 'Kallakurichi Road',
            'latitude': 11.7374,
            'longitude': 78.9634,
            'rating': 4.5,
            'phone': '9876543212',
            'price_range': '₹₹',
            'timing': '24 Hours',
            'rooms_available': 8,
            'base_price': 2200.00,
            'source': 'booking'
        },
        {
            'name': 'Royal Palace',
            'vendor_type': 'hotel',
            'description': 'Experience royalty at affordable prices.',
            'address': 'Thanjavur Highway',
            'latitude': 10.7850,
            'longitude': 79.1378,
            'rating': 4.6,
            'phone': '9876543213',
            'price_range': '₹₹₹',
            'timing': '24 Hours',
            'rooms_available': 3,
            'base_price': 4500.00,
            'source': 'yatra'
        },
        {
            'name': 'Budget Stay',
            'vendor_type': 'hotel',
            'description': 'Cheap and clean rooms for quick stays.',
            'address': 'Railway Station Road, Trichy',
            'latitude': 10.7900,
            'longitude': 78.6900,
            'rating': 3.8,
            'phone': '9876543218',
            'price_range': '₹',
            'timing': '24 Hours',
            'rooms_available': 20,
            'base_price': 800.00,
            'source': 'booking'
        },
        {
            'name': 'Highway Rest Inn',
            'vendor_type': 'hotel',
            'description': 'Spacious rooms with garden view.',
            'address': 'Villupuram Highway',
            'latitude': 11.9500,
            'longitude': 79.5000,
            'rating': 4.4,
            'phone': '9876543219',
            'price_range': '₹₹',
            'timing': '24 Hours',
            'rooms_available': 4,
            'base_price': 1800.00,
            'source': 'goibibo'
        },
        # Food & Restaurants
        {
            'name': 'Highway Dhaba',
            'vendor_type': 'food',
            'description': 'Traditional dhabha style food. Best for parathas and chai.',
            'address': 'NH 45, Near Toll Plaza',
            'latitude': 11.4567,
            'longitude': 78.9876,
            'rating': 4.5,
            'phone': '9876543214',
            'price_range': '₹',
            'timing': '6:00 AM - 12:00 AM',
            'base_price': 150.00,
            'source': 'direct'
        },
        {
            'name': 'South Indian Tiffin Center',
            'vendor_type': 'food',
            'description': 'Authentic idli, dosa and filter coffee.',
            'address': 'Main Road, Villupuram',
            'latitude': 11.9401,
            'longitude': 79.4861,
            'rating': 4.3,
            'phone': '9876543215',
            'price_range': '₹',
            'timing': '7:00 AM - 10:00 PM',
            'base_price': 80.00,
            'source': 'direct'
        },
        {
            'name': 'Punjabi Rasoi',
            'vendor_type': 'food',
            'description': 'Delicious North Indian cuisine.',
            'address': 'Trichy City Center',
            'latitude': 10.8305,
            'longitude': 78.7047,
            'rating': 4.6,
            'phone': '9876543216',
            'price_range': '₹₹',
            'timing': '11:00 AM - 11:00 PM',
            'base_price': 400.00,
            'source': 'direct'
        },
        {
            'name': 'Cafe Coffee Day',
            'vendor_type': 'food',
            'description': 'Coffee and snacks. Perfect for a quick break.',
            'address': 'NH 45 Highway',
            'latitude': 11.6500,
            'longitude': 79.1000,
            'rating': 4.0,
            'phone': '9876543217',
            'price_range': '₹₹',
            'timing': '24 Hours',
            'base_price': 250.00,
            'source': 'direct'
        },
        # Workshops
        {
            'name': 'Speed Kings Workshop',
            'vendor_type': 'workshop',
            'description': 'Specialized in multi-brand bike service and puncture works.',
            'address': 'Old Bus Stand, Perambalur',
            'latitude': 11.2312,
            'longitude': 78.8765,
            'rating': 4.7,
            'phone': '9944556677',
            'price_range': '₹',
            'timing': '8:00 AM - 10:00 PM',
            'rooms_available': 0,
            'base_price': 200.00,
            'source': 'direct',
            'availability_status': 'Available'
        },
        {
            'name': 'Puncture Point 24/7',
            'vendor_type': 'workshop',
            'description': '24/7 Roadside assistance and quick puncture fixes.',
            'address': 'NH 45 Highway',
            'latitude': 11.1500,
            'longitude': 78.9000,
            'rating': 4.3,
            'phone': '9944556688',
            'price_range': '₹',
            'timing': '24 Hours',
            'rooms_available': 0,
            'base_price': 150.00,
            'source': 'direct',
            'availability_status': 'Busy'
        },
        {
            'name': 'Expert Mechanics',
            'vendor_type': 'workshop',
            'description': 'Expert mechanics for car and bike repairs.',
            'address': 'Trichy Townhall',
            'latitude': 10.8282,
            'longitude': 78.6948,
            'rating': 4.5,
            'phone': '9944556699',
            'price_range': '₹₹',
            'timing': '9:00 AM - 8:00 PM',
            'rooms_available': 0,
            'base_price': 500.00,
            'source': 'direct',
            'availability_status': 'Available'
        },
        {
            'name': 'Quick Puncture Repair',
            'vendor_type': 'workshop',
            'description': 'Fast puncture repair for all vehicles.',
            'address': 'Kallakurichi Bypass',
            'latitude': 11.7300,
            'longitude': 78.9600,
            'rating': 4.1,
            'phone': '9944556700',
            'price_range': '₹',
            'timing': '7:00 AM - 9:00 PM',
            'rooms_available': 0,
            'base_price': 100.00,
            'source': 'direct',
            'availability_status': 'Available'
        },
        {
            'name': '24x7 Roadside Assistance',
            'vendor_type': 'workshop',
            'description': 'Help is just a call away, any time.',
            'address': 'Chennai Highway',
            'latitude': 12.8300,
            'longitude': 79.7000,
            'rating': 4.9,
            'phone': '9944556701',
            'price_range': '₹₹',
            'timing': '24 Hours',
            'rooms_available': 0,
            'base_price': 1000.00,
            'source': 'direct',
            'availability_status': 'Available'
        }
    ]
    
    for v_data in vendors:
        Vendor.objects.create(**v_data)
    
    print(f"Successfully seeded {len(vendors)} vendors.")
    
    from core_api.models import EmergencyService
    EmergencyService.objects.all().delete()
    
    emergency_services = [
        {
            'name': 'City General Hospital',
            'service_type': 'hospital',
            'phone': '04328-123456',
            'address': 'Medical College Road, Trichy',
            'latitude': 10.8200,
            'longitude': 78.6800,
            'is_24x7': True
        },
        {
            'name': 'Central Police Station',
            'service_type': 'police',
            'phone': '100',
            'address': 'Main Bazaar, Perambalur',
            'latitude': 11.2333,
            'longitude': 78.8833,
            'is_24x7': True
        },
        {
            'name': 'Highway Rescue Ambulance',
            'service_type': 'ambulance',
            'phone': '108',
            'address': 'NH 45 Toll Plaza',
            'latitude': 11.4500,
            'longitude': 78.9800,
            'is_24x7': True
        }
    ]
    
    for e_data in emergency_services:
        EmergencyService.objects.create(**e_data)
    
    print(f"Successfully seeded {len(emergency_services)} emergency services.")

if __name__ == '__main__':
    seed_data()
