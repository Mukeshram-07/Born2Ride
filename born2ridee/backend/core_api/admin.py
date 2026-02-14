from django.contrib import admin
from .models import Trip, Vendor, EmergencyService


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ['id', 'origin', 'destination', 'vehicle_type', 'distance_km', 'fuel_cost', 'created_at']
    list_filter = ['vehicle_type', 'created_at']
    search_fields = ['origin', 'destination']
    readonly_fields = ['created_at']


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'vendor_type', 'rating', 'phone', 'is_open']
    list_filter = ['vendor_type', 'is_open', 'rating']
    search_fields = ['name', 'address']


@admin.register(EmergencyService)
class EmergencyServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'service_type', 'phone', 'is_24x7']
    list_filter = ['service_type', 'is_24x7']
    search_fields = ['name', 'address', 'phone']
