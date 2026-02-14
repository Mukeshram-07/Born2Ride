from rest_framework import serializers
from .models import Trip, Vendor, EmergencyService, Booking


class TripSerializer(serializers.ModelSerializer):
    """Serializer for Trip model"""
    
    class Meta:
        model = Trip
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'fuel_cost', 'fuel_liters']


class TripCreateSerializer(serializers.Serializer):
    """Serializer for creating a trip with fuel calculation"""
    origin = serializers.CharField(max_length=255)
    destination = serializers.CharField(max_length=255)
    origin_lat = serializers.FloatField(default=0.0)
    origin_lng = serializers.FloatField(default=0.0)
    dest_lat = serializers.FloatField(default=0.0)
    dest_lng = serializers.FloatField(default=0.0)
    distance_km = serializers.FloatField()
    vehicle_type = serializers.ChoiceField(choices=['bike', 'car'])
    stops_visited = serializers.ListField(child=serializers.DictField(), required=False, default=list)


class FuelCalculationSerializer(serializers.Serializer):
    """Serializer for fuel cost calculation request"""
    distance_km = serializers.FloatField(min_value=0)
    vehicle_type = serializers.ChoiceField(choices=['bike', 'car'])
    fuel_price = serializers.FloatField(min_value=0, default=104.0)  # Default petrol price


class FuelCalculationResponseSerializer(serializers.Serializer):
    """Serializer for fuel cost calculation response"""
    distance_km = serializers.FloatField()
    vehicle_type = serializers.CharField()
    mileage_kmpl = serializers.FloatField()
    fuel_liters = serializers.FloatField()
    fuel_price_per_liter = serializers.FloatField()
    total_fuel_cost = serializers.FloatField()


class VendorSerializer(serializers.ModelSerializer):
    """Serializer for Vendor model"""
    vendor_type_display = serializers.CharField(source='get_vendor_type_display', read_only=True)
    source_display = serializers.CharField(source='get_source_display', read_only=True)
    
    class Meta:
        model = Vendor
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    """Serializer for Booking model"""
    vendor_name = serializers.CharField(source='vendor.name', read_only=True)
    
    class Meta:
        model = Booking
        fields = '__all__'


class EmergencyServiceSerializer(serializers.ModelSerializer):
    """Serializer for EmergencyService model"""
    service_type_display = serializers.CharField(source='get_service_type_display', read_only=True)
    
    class Meta:
        model = EmergencyService
        fields = '__all__'
