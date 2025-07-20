from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Listing, Booking

User = get_user_model()


class ListingSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=1000)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    location = serializers.CharField(max_length=255)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Listing
        fields = [
            'listing_id', 'user_id', 'title', 'description', 
            'price', 'location', 'created_at', 'updated_at'
        ]


class BookingSerializer(serializers.ModelSerializer):
    booking_id = serializers.UUIDField(read_only=True)
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Booking
        fields = [
            'booking_id', 'listing_id', 'user_id', 
            'start_date', 'end_date', 'created_at'
        ]
        
    def validate(self, data):
        if data['start_date'] >= data['end_date']:
            raise serializers.ValidationError("Start date must be before end date.")
        return data
