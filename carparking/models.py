from django.db import models

class ParkingSlots(models.Model):
    slot_id = models.IntegerField()
    distance = models.IntegerField()
    availibility_status = models.BooleanField(default=True)
    car_registration_number = models.CharField(max_length=200,blank=True)
    car_color = models.CharField(max_length=200,blank=True)


