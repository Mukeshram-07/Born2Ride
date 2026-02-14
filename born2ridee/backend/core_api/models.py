from django.db import models


class Trip(models.Model):
    """Model to store trip information"""
    VEHICLE_CHOICES = [
        ('bike', 'Bike'),
        ('car', 'Car'),
    ]
    
    origin = models.CharField(max_length=255, help_text="Starting location")
    destination = models.CharField(max_length=255, help_text="Destination location")
    origin_lat = models.FloatField(default=0.0)
    origin_lng = models.FloatField(default=0.0)
    dest_lat = models.FloatField(default=0.0)
    dest_lng = models.FloatField(default=0.0)
    distance_km = models.FloatField(help_text="Distance in kilometers")
    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_CHOICES)
    fuel_cost = models.FloatField(help_text="Estimated fuel cost in INR")
    fuel_liters = models.FloatField(default=0.0, help_text="Fuel required in liters")
    stops_visited = models.JSONField(default=list, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.origin} → {self.destination} ({self.vehicle_type})"


class Vendor(models.Model):
    """Model for food vendors, hotels, and workshops"""
    VENDOR_TYPES = [
        ('food', 'Food & Restaurant'),
        ('hotel', 'Hotel & Lodge'),
        ('workshop', 'Puncture & Workshop'),
    ]
    
    SOURCE_CHOICES = [
        ('direct', 'Direct'),
        ('goibibo', 'Goibibo'),
        ('mmt', 'MakeMyTrip'),
        ('yatra', 'Yatra'),
        ('booking', 'Booking.com'),
    ]
    
    name = models.CharField(max_length=100)
    vendor_type = models.CharField(max_length=20, choices=VENDOR_TYPES)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    rating = models.FloatField(default=4.0)
    phone = models.CharField(max_length=15)
    image_url = models.URLField(blank=True)
    is_open = models.BooleanField(default=True)
    price_range = models.CharField(max_length=10, default='₹₹', help_text="Price range indicator")
    
    # New fields for enhanced functionality
    timing = models.CharField(max_length=100, default="9:00 AM - 9:00 PM", help_text="Opening and closing hours")
    rooms_available = models.IntegerField(default=0, help_text="Number of rooms available (for hotels)")
    base_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, help_text="Base price for room or service")
    source = models.CharField(max_length=20, choices=SOURCE_CHOICES, default='direct')
    availability_status = models.CharField(max_length=20, default="Available", help_text="Status for workshops (Available/Busy)")
    
    class Meta:
        ordering = ['-rating']
    
    def __str__(self):
        return f"{self.name} ({self.get_vendor_type_display()})"


class Booking(models.Model):
    """Model for hotel and workshop bookings"""
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]
    
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='bookings')
    customer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    check_in = models.DateTimeField(null=True, blank=True)
    check_out = models.DateTimeField(null=True, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Booking for {self.customer_name} at {self.vendor.name}"


class EmergencyService(models.Model):
    """Model for emergency services like police, hospitals, ambulance"""
    SERVICE_TYPES = [
        ('police', 'Police Station'),
        ('hospital', 'Hospital'),
        ('ambulance', 'Ambulance Service'),
        ('fire', 'Fire Station'),
        ('roadside', 'Roadside Assistance'),
    ]
    
    name = models.CharField(max_length=100)
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPES)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    is_24x7 = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['service_type', 'name']
        verbose_name_plural = "Emergency Services"
    
    def __str__(self):
        return f"{self.name} - {self.phone}"
