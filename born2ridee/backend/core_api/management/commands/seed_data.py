"""
Management command to seed the database with sample data for Born 2 Ride MVP
"""
from django.core.management.base import BaseCommand
from core_api.models import Vendor, EmergencyService


class Command(BaseCommand):
    help = 'Seeds the database with sample vendors and emergency services'

    def handle(self, *args, **options):
        self.stdout.write('Seeding database...')
        
        # Clear existing data
        Vendor.objects.all().delete()
        EmergencyService.objects.all().delete()
        
        # Seed Vendors - Food
        food_vendors = [
            {
                'name': 'Highway Dhaba',
                'vendor_type': 'food',
                'description': 'Authentic North Indian highway dhaba with famous dal makhani and butter chicken',
                'address': 'NH-44, Km 125, Near Toll Plaza',
                'latitude': 13.0827,
                'longitude': 80.2707,
                'rating': 4.5,
                'phone': '+91 98765 43210',
                'price_range': '₹₹',
                'is_open': True,
            },
            {
                'name': 'Café Coffee Day',
                'vendor_type': 'food',
                'description': 'Quick bites and refreshing beverages for tired travelers',
                'address': 'Service Road, Near Petrol Pump',
                'latitude': 13.0900,
                'longitude': 80.2800,
                'rating': 4.2,
                'phone': '+91 98765 43211',
                'price_range': '₹₹₹',
                'is_open': True,
            },
            {
                'name': 'South Indian Tiffin Center',
                'vendor_type': 'food',
                'description': 'Fresh dosas, idlis, and authentic filter coffee',
                'address': 'Main Road, Opposite Bus Stand',
                'latitude': 13.0750,
                'longitude': 80.2650,
                'rating': 4.7,
                'phone': '+91 98765 43212',
                'price_range': '₹',
                'is_open': True,
            },
            {
                'name': 'Punjabi Rasoi',
                'vendor_type': 'food',
                'description': 'Thali meals and fresh rotis made on tandoor',
                'address': 'Highway Junction, Near Flyover',
                'latitude': 13.1000,
                'longitude': 80.2900,
                'rating': 4.3,
                'phone': '+91 98765 43213',
                'price_range': '₹₹',
                'is_open': True,
            },
        ]
        
        # Seed Vendors - Hotels
        hotel_vendors = [
            {
                'name': 'Highway Rest Inn',
                'vendor_type': 'hotel',
                'description': 'Budget-friendly rooms with AC, TV, and attached bathroom',
                'address': 'NH-44, Km 130, Beside Petrol Pump',
                'latitude': 13.0850,
                'longitude': 80.2750,
                'rating': 4.0,
                'phone': '+91 98765 43220',
                'price_range': '₹₹',
                'is_open': True,
            },
            {
                'name': 'Travelers Lodge',
                'vendor_type': 'hotel',
                'description': 'Comfortable stay with parking, WiFi, and 24x7 room service',
                'address': 'Service Road, Near Highway Exit',
                'latitude': 13.0950,
                'longitude': 80.2850,
                'rating': 4.4,
                'phone': '+91 98765 43221',
                'price_range': '₹₹₹',
                'is_open': True,
            },
            {
                'name': 'Budget Stay',
                'vendor_type': 'hotel',
                'description': 'Affordable dormitory and private rooms for solo travelers',
                'address': 'Main Market, Near Bus Station',
                'latitude': 13.0800,
                'longitude': 80.2680,
                'rating': 3.8,
                'phone': '+91 98765 43222',
                'price_range': '₹',
                'is_open': True,
            },
        ]
        
        # Seed Vendors - Workshops
        workshop_vendors = [
            {
                'name': 'Quick Puncture Repair',
                'vendor_type': 'workshop',
                'description': 'Fast puncture repair, air filling, and basic bike servicing',
                'address': 'Highway Service Road, Near Milestone 128',
                'latitude': 13.0880,
                'longitude': 80.2780,
                'rating': 4.6,
                'phone': '+91 98765 43230',
                'price_range': '₹',
                'is_open': True,
            },
            {
                'name': 'AutoCare Service Center',
                'vendor_type': 'workshop',
                'description': 'Full car service, oil change, and emergency repairs',
                'address': 'Industrial Area, Near Highway',
                'latitude': 13.0920,
                'longitude': 80.2820,
                'rating': 4.3,
                'phone': '+91 98765 43231',
                'price_range': '₹₹',
                'is_open': True,
            },
            {
                'name': 'Two Wheeler Experts',
                'vendor_type': 'workshop',
                'description': 'Specialized in bike repairs, spare parts, and modifications',
                'address': 'Main Road, Opposite Petrol Bunk',
                'latitude': 13.0780,
                'longitude': 80.2700,
                'rating': 4.5,
                'phone': '+91 98765 43232',
                'price_range': '₹',
                'is_open': True,
            },
            {
                'name': '24x7 Roadside Assistance',
                'vendor_type': 'workshop',
                'description': 'Emergency towing, jump start, and on-spot repairs',
                'address': 'Available on Call - All Highway Areas',
                'latitude': 13.0900,
                'longitude': 80.2750,
                'rating': 4.8,
                'phone': '+91 98765 43233',
                'price_range': '₹₹₹',
                'is_open': True,
            },
        ]
        
        # Create all vendors
        all_vendors = food_vendors + hotel_vendors + workshop_vendors
        for vendor_data in all_vendors:
            Vendor.objects.create(**vendor_data)
        
        self.stdout.write(self.style.SUCCESS(f'Created {len(all_vendors)} vendors'))
        
        # Seed Emergency Services
        emergency_services = [
            {
                'name': 'Highway Police Control Room',
                'service_type': 'police',
                'phone': '100',
                'address': 'NH-44, Police Outpost',
                'latitude': 13.0860,
                'longitude': 80.2760,
                'is_24x7': True,
            },
            {
                'name': 'Traffic Police Helpline',
                'service_type': 'police',
                'phone': '103',
                'address': 'District Traffic Office',
                'latitude': 13.0840,
                'longitude': 80.2740,
                'is_24x7': True,
            },
            {
                'name': 'Government General Hospital',
                'service_type': 'hospital',
                'phone': '+91 44 2530 5000',
                'address': 'Park Town, Near Central Station',
                'latitude': 13.0890,
                'longitude': 80.2790,
                'is_24x7': True,
            },
            {
                'name': 'Apollo Emergency Care',
                'service_type': 'hospital',
                'phone': '+91 44 2829 3333',
                'address': 'Greams Road, Near Highway Junction',
                'latitude': 13.0870,
                'longitude': 80.2770,
                'is_24x7': True,
            },
            {
                'name': '108 Ambulance Service',
                'service_type': 'ambulance',
                'phone': '108',
                'address': 'Emergency Medical Services',
                'latitude': 13.0850,
                'longitude': 80.2750,
                'is_24x7': True,
            },
            {
                'name': 'Private Ambulance Network',
                'service_type': 'ambulance',
                'phone': '+91 98765 00108',
                'address': 'Quick Response Medical Services',
                'latitude': 13.0830,
                'longitude': 80.2730,
                'is_24x7': True,
            },
            {
                'name': 'Fire and Rescue',
                'service_type': 'fire',
                'phone': '101',
                'address': 'Fire Station, Main Road',
                'latitude': 13.0820,
                'longitude': 80.2720,
                'is_24x7': True,
            },
            {
                'name': 'RSA Roadside Assistance',
                'service_type': 'roadside',
                'phone': '+91 1800 123 4567',
                'address': 'Pan India Coverage',
                'latitude': 13.0900,
                'longitude': 80.2800,
                'is_24x7': True,
            },
        ]
        
        for service_data in emergency_services:
            EmergencyService.objects.create(**service_data)
        
        self.stdout.write(self.style.SUCCESS(f'Created {len(emergency_services)} emergency services'))
        self.stdout.write(self.style.SUCCESS('Database seeding completed!'))
