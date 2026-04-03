from django.forms import ModelForm
from .models import SlotBooking


# Code added for loading form data on the Booking page
class BookingForm(ModelForm):
    class Meta:
        model = SlotBooking
        fields = "__all__"
