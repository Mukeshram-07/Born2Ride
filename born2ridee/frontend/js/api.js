/**
 * Born 2 Ride - API Integration Module
 * Handles all communication with the Django REST API
 */

const API_BASE_URL = `http://${window.location.hostname}:8000/api`;
console.log('Born 2 Ride API Initialized. Base URL:', API_BASE_URL);


/**
 * API Client for Born 2 Ride Backend
 */
const API = {
    /**
     * Make a GET request
     */
    async get(endpoint) {
        try {
            const response = await fetch(`${API_BASE_URL}${endpoint}`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                },
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            return await response.json();
        } catch (error) {
            console.error('API GET Error:', error);
            throw error;
        }
    },

    /**
     * Make a POST request
     */
    async post(endpoint, data) {
        try {
            const response = await fetch(`${API_BASE_URL}${endpoint}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            return await response.json();
        } catch (error) {
            console.error('API POST Error:', error);
            throw error;
        }
    },

    // ============ TRIP ENDPOINTS ============

    /**
     * Create a new trip
     */
    async createTrip(tripData) {
        return this.post('/trips/', tripData);
    },

    /**
     * Get all trips
     */
    async getTrips() {
        return this.get('/trips/');
    },

    /**
     * Get a specific trip by ID
     */
    async getTrip(tripId) {
        return this.get(`/trips/${tripId}/`);
    },

    // ============ FUEL CALCULATION ============

    /**
     * Calculate fuel cost
     * @param {number} distanceKm - Distance in kilometers
     * @param {string} vehicleType - 'bike' or 'car'
     * @param {number} fuelPrice - Optional fuel price per liter
     */
    async calculateFuel(distanceKm, vehicleType, fuelPrice = 104.0) {
        return this.post('/calculate-fuel/', {
            distance_km: distanceKm,
            vehicle_type: vehicleType,
            fuel_price: fuelPrice,
        });
    },

    // ============ VENDOR ENDPOINTS ============

    /**
     * Get all vendors
     * @param {string} type - Optional filter: 'food', 'hotel', 'workshop'
     */
    async getVendors(type = null) {
        const endpoint = type ? `/vendors/?type=${type}` : '/vendors/';
        return this.get(endpoint);
    },

    /**
     * Get food vendors
     */
    async getFoodVendors() {
        return this.getVendors('food');
    },

    /**
     * Get hotels
     */
    async getHotels() {
        return this.getVendors('hotel');
    },

    /**
     * Get workshops
     */
    async getWorkshops() {
        return this.getVendors('workshop');
    },

    // ============ EMERGENCY ENDPOINTS ============

    /**
     * Get all emergency services
     * @param {string} type - Optional filter: 'police', 'hospital', 'ambulance', 'fire', 'roadside'
     */
    async getEmergencyServices(type = null) {
        const endpoint = type ? `/emergency/?type=${type}` : '/emergency/';
        return this.get(endpoint);
    },

    /**
     * Get police stations
     */
    async getPoliceStations() {
        return this.getEmergencyServices('police');
    },

    /**
     * Get hospitals
     */
    async getHospitals() {
        return this.getEmergencyServices('hospital');
    },

    /**
     * Get ambulance services
     */
    async getAmbulances() {
        return this.getEmergencyServices('ambulance');
    },
};

/**
 * Storage Helper for Trip Data
 */
const TripStorage = {
    KEY: 'born2ride_trip',

    /**
     * Save current trip data to localStorage
     */
    save(tripData) {
        localStorage.setItem(this.KEY, JSON.stringify(tripData));
    },

    /**
     * Get current trip data from localStorage
     */
    get() {
        const data = localStorage.getItem(this.KEY);
        return data ? JSON.parse(data) : null;
    },

    /**
     * Clear trip data
     */
    clear() {
        localStorage.removeItem(this.KEY);
    },

    /**
     * Update trip data partially
     */
    update(updates) {
        const current = this.get() || {};
        const updated = { ...current, ...updates };
        this.save(updated);
        return updated;
    },

    /**
     * Add a stop to the trip
     */
    addStop(stop) {
        const trip = this.get() || { stops: [] };
        trip.stops = trip.stops || [];
        trip.stops.push(stop);
        this.save(trip);
    },
};

/**
 * Utility Functions
 */
const Utils = {
    /**
     * Format currency in INR
     */
    formatCurrency(amount) {
        return new Intl.NumberFormat('en-IN', {
            style: 'currency',
            currency: 'INR',
            minimumFractionDigits: 0,
            maximumFractionDigits: 0,
        }).format(amount);
    },

    /**
     * Format distance
     */
    formatDistance(km) {
        return `${km.toFixed(1)} km`;
    },

    /**
     * Calculate distance between two coordinates (Haversine formula)
     */
    calculateDistance(lat1, lon1, lat2, lon2) {
        const R = 6371; // Earth's radius in km
        const dLat = this.toRad(lat2 - lat1);
        const dLon = this.toRad(lon2 - lon1);
        const a =
            Math.sin(dLat / 2) * Math.sin(dLat / 2) +
            Math.cos(this.toRad(lat1)) * Math.cos(this.toRad(lat2)) *
            Math.sin(dLon / 2) * Math.sin(dLon / 2);
        const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
        return R * c;
    },

    toRad(deg) {
        return deg * (Math.PI / 180);
    },

    /**
     * Show toast notification
     */
    showToast(message, type = 'success') {
        const existingToast = document.querySelector('.toast');
        if (existingToast) {
            existingToast.remove();
        }

        const toast = document.createElement('div');
        toast.className = `toast ${type}`;
        toast.innerHTML = `
            <span class="toast-icon">${type === 'success' ? '✓' : '✕'}</span>
            <span class="toast-message">${message}</span>
        `;

        document.body.appendChild(toast);

        // Trigger animation
        setTimeout(() => toast.classList.add('show'), 10);

        // Remove after 3 seconds
        setTimeout(() => {
            toast.classList.remove('show');
            setTimeout(() => toast.remove(), 300);
        }, 3000);
    },

    /**
     * Get vendor icon based on type
     */
    getVendorIcon(type) {
        const icons = {
            food: '🍽️',
            hotel: '🏨',
            workshop: '🔧',
        };
        return icons[type] || '📍';
    },

    /**
     * Get emergency icon based on type
     */
    getEmergencyIcon(type) {
        const icons = {
            police: '🚔',
            hospital: '🏥',
            ambulance: '🚑',
            fire: '🚒',
            roadside: '🚗',
        };
        return icons[type] || '📞';
    },

    /**
     * Render star rating
     */
    renderStars(rating) {
        const fullStars = Math.floor(rating);
        const hasHalfStar = rating % 1 >= 0.5;
        let stars = '★'.repeat(fullStars);
        if (hasHalfStar) stars += '½';
        stars += '☆'.repeat(5 - fullStars - (hasHalfStar ? 1 : 0));
        return stars;
    },
};

// Global error handling
window.addEventListener('error', function (event) {
    console.error('Global Error:', event.error);
    if (window.Utils) {
        window.Utils.showToast('Application Error: ' + (event.error?.message || 'Something went wrong'), 'error');
    }
});

window.addEventListener('unhandledrejection', function (event) {
    console.error('Unhandled Rejection:', event.reason);
    if (window.Utils) {
        window.Utils.showToast('Server connection error. Please ensure the backend is running.', 'error');
    }
});

// Make available globally
window.API = API;
window.TripStorage = TripStorage;
window.Utils = Utils;
