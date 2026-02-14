from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q
from .models import Trip, Vendor, EmergencyService, Booking
from .serializers import (
    TripSerializer, TripCreateSerializer,
    VendorSerializer, EmergencyServiceSerializer,
    FuelCalculationSerializer, FuelCalculationResponseSerializer,
    BookingSerializer
)


# Fuel mileage constants (km per liter)
VEHICLE_MILEAGE = {
    'bike': 45,  # Average bike mileage
    'car': 15,   # Average car mileage
}

# Default fuel price (INR per liter)
DEFAULT_FUEL_PRICE = 104.0


def calculate_fuel_cost(distance_km, vehicle_type, fuel_price=DEFAULT_FUEL_PRICE):
    """Calculate fuel cost based on distance and vehicle type"""
    mileage = VEHICLE_MILEAGE.get(vehicle_type, 15)
    fuel_liters = distance_km / mileage
    total_cost = fuel_liters * fuel_price
    return {
        'mileage_kmpl': mileage,
        'fuel_liters': round(fuel_liters, 2),
        'fuel_price_per_liter': fuel_price,
        'total_fuel_cost': round(total_cost, 2)
    }


class TripViewSet(viewsets.ModelViewSet):
    """ViewSet for Trip CRUD operations"""
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    
    def create(self, request, *args, **kwargs):
        """Create a trip with automatic fuel calculation"""
        serializer = TripCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        
        # Calculate fuel cost
        fuel_data = calculate_fuel_cost(
            data['distance_km'],
            data['vehicle_type']
        )
        
        # Create trip with calculated values
        trip = Trip.objects.create(
            origin=data['origin'],
            destination=data['destination'],
            origin_lat=data.get('origin_lat', 0),
            origin_lng=data.get('origin_lng', 0),
            dest_lat=data.get('dest_lat', 0),
            dest_lng=data.get('dest_lng', 0),
            distance_km=data['distance_km'],
            vehicle_type=data['vehicle_type'],
            fuel_cost=fuel_data['total_fuel_cost'],
            fuel_liters=fuel_data['fuel_liters'],
            stops_visited=data.get('stops_visited', [])
        )
        
        response_serializer = TripSerializer(trip)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)


class VendorViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for Vendor read operations"""
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    
    def get_queryset(self):
        """Filter vendors by type if provided"""
        queryset = Vendor.objects.all()
        vendor_type = self.request.query_params.get('type', None)
        is_open = self.request.query_params.get('is_open', None)
        source = self.request.query_params.get('source', None)
        
        if vendor_type:
            queryset = queryset.filter(vendor_type=vendor_type)
        if is_open is not None:
            queryset = queryset.filter(is_open=is_open.lower() == 'true')
        if source:
            queryset = queryset.filter(source=source)
        
        return queryset


class BookingViewSet(viewsets.ModelViewSet):
    """ViewSet for Booking operations"""
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
    def create(self, request, *args, **kwargs):
        vendor_id = request.data.get('vendor')
        try:
            vendor = Vendor.objects.get(id=vendor_id)
            if vendor.vendor_type == 'hotel' and vendor.rooms_available <= 0:
                return Response({'error': 'No rooms available'}, status=status.HTTP_400_BAD_REQUEST)
            
            # Reduce room count if it's a hotel
            if vendor.vendor_type == 'hotel':
                vendor.rooms_available -= 1
                vendor.save()
                
        except Vendor.DoesNotExist:
            return Response({'error': 'Vendor not found'}, status=status.HTTP_404_NOT_FOUND)
            
        return super().create(request, *args, **kwargs)


class EmergencyServiceViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for EmergencyService read operations"""
    queryset = EmergencyService.objects.all()
    serializer_class = EmergencyServiceSerializer
    
    def get_queryset(self):
        """Filter emergency services by type if provided"""
        queryset = EmergencyService.objects.all()
        service_type = self.request.query_params.get('type', None)
        
        if service_type:
            queryset = queryset.filter(service_type=service_type)
        
        return queryset


class CalculateFuelView(APIView):
    """API endpoint to calculate fuel cost"""
    
    def post(self, request):
        serializer = FuelCalculationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        
        fuel_data = calculate_fuel_cost(
            data['distance_km'],
            data['vehicle_type'],
            data.get('fuel_price', DEFAULT_FUEL_PRICE)
        )
        
        response_data = {
            'distance_km': data['distance_km'],
            'vehicle_type': data['vehicle_type'],
            **fuel_data
        }
        
        return Response(response_data, status=status.HTTP_200_OK)


@api_view(['GET'])
def api_overview(request):
    """API overview endpoint"""
    return Response({
        'message': 'Welcome to Born 2 Ride API',
        'version': '1.0.0',
        'endpoints': {
            'vendors': '/api/vendors/',
            'vendors_by_type': '/api/vendors/?type=food|hotel|workshop',
            'bookings': '/api/bookings/',
            'emergency_services': '/api/emergency/',
            'trips': '/api/trips/',
            'calculate_fuel': '/api/calculate-fuel/',
        }
    })
