from rest_framework import serializers
from .models import Menu, SlotBooking

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlotBooking   # <-- si tu modelo se llama Booking, cambiá esto a Booking
        fields = "__all__"