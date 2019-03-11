from django.template import loader
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.template import Context
import json 
from .models import ParkingSlots
from django.http import QueryDict

def create_new_parking(total_num_slot):
	for slot in range(1,int(total_num_slot)+1):
			v,created=ParkingSlots.objects.get_or_create(slot_id=slot,distance=slot)

# add slots to existing parking lot
def add_slot_to_parking(add_num):
	last = ParkingSlots.objects.last()
	distance = last.distance
	for dis in range(distance+1,distance+int(add_num)):
		v,created=ParkingSlots.objects.get_or_create(slot_id=dis,distance=dis)

def slot_status_inparking(get_slot_status):
	slot_status = ""
	slot_status = ParkingSlots.objects.get(slot_id=get_slot_status).availibility_status
	if not slot_status:
		slot_status="Car is parked in slot"
	else:
		slot_status="Car is not parked"	
	return slot_status
# to allocate slots to cars
def allocate_slot(car_registration_num,car_color):
	available_slot = ParkingSlots.objects.filter(availibility_status=True).order_by('distance')
	error_message = ""
	if not 	available_slot:
		error_message = "There are no available_slot to park your car"

	available_slot[0].car_registration_number=car_registration_num
	available_slot[0].car_color=car_color
	available_slot[0].availibility_status=False
	available_slot[0].save()

	return error_message

#to empty the slots for cars
def vacant_slot(slot_id):
	slot = ParkingSlots.objects.get(slot_id=slot_id)
	error_message=""
	if not slot:
		error_message="Following slot_id not available in Parking Lot" 

	slot.car_registration_num=""
	slot.car_color=""
	slot.availibility_status=True
	slot.save()
	return error_message
