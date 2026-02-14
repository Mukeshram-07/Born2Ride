from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'trips', views.TripViewSet, basename='trip')
router.register(r'vendors', views.VendorViewSet, basename='vendor')
router.register(r'bookings', views.BookingViewSet, basename='booking')
router.register(r'emergency', views.EmergencyServiceViewSet, basename='emergency')

urlpatterns = [
    path('', views.api_overview, name='api-overview'),
    path('', include(router.urls)),
    path('calculate-fuel/', views.CalculateFuelView.as_view(), name='calculate-fuel'),
]
