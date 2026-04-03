# from django.db import models


# # Create your models here.
# class Booking(models.Model):
#     first_name = models.CharField(max_length=200)
#     reservation_date = models.DateField()
#     reservation_slot = models.SmallIntegerField(default=10)

#     def __str__(self): 
#         return self.first_name


# # Add code to create Menu model
# class Menu(models.Model):
#    name = models.CharField(max_length=200) 
#    price = models.IntegerField(null=False) 
#    menu_item_description = models.TextField(max_length=1000, default='') 

#    def __str__(self):
#       return self.name

from django.db import models

# (1) Tu modelo viejo, renombrado para no chocar con el capstone
class SlotBooking(models.Model):
    first_name = models.CharField(max_length=200)
    reservation_date = models.DateField()
    reservation_slot = models.SmallIntegerField()

    def __str__(self):
        return f"{self.first_name} - {self.reservation_date} ({self.reservation_slot})"


# (2) Modelo CAPSTONE: Booking (schema del enunciado)
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.booking_date} ({self.no_of_guests})"


# (3) Modelo CAPSTONE: Menu (schema del enunciado)
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return f'{self.title} : {self.price}'
