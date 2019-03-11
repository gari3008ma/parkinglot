from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.template import Context
import json 
from .models import ParkingSlots
from django.http import QueryDict
from .parking_utils import allocate_slot,vacant_slot,create_new_parking,add_slot_to_parking,slot_status_inparking

#Used Django templates to render frontend .Html templates that are being rendered are in templates folder

# Create your views here.
# create dashboard view for first page and take input the number of slots that we want to have in our parking lot
@csrf_protect
def index(request):
	#Todo add slot to parking lot
	if request.method == 'POST':
		data =  QueryDict(request.body).dict()
		total_num_slot=data.get('slot_numbers','')
		add_num=data.get('add_slot','')
		if add_num:
			add_slot_to_parking(add_num)
		if total_num_slot:
			create_new_parking(total_num_slot)

	template = loader.get_template('carparking/index.html')
	return render(request, 'carparking/index.html')

# will add car to parking slots ,throw error when no more slot available and also vacant to given slot id
# will use pg_advisory lock when two people make request at same time
# return error when slot number to be vacanted not present
@csrf_protect
def dashboard(request):
	error_message=""
	slot_status=""
	if request.method == 'POST':
		data =  QueryDict(request.body).dict()
		car_registration_num = data.get('car_registration_num','')
		car_color = data.get('car_color','')
		slot_id = data.get('slot_number','')
		get_slot_status = data.get('slot_status','')
		if car_registration_num and car_color:
			error_message = allocate_slot(car_registration_num,car_color)
		if slot_id:
			error_message = vacant_slot(slot_id)
		if get_slot_status:
			slot_status=slot_status_inparking(get_slot_status)
	template = loader.get_template('carparking/dashboard.html')
	return render(request, 'carparking/dashboard.html',{"error_message":error_message,"status":str(slot_status)})


# print slot id with car_number and color that are avaliable in parking lot
@csrf_protect
def get_all_slots(request):
	all_slots=ParkingSlots.objects.filter(availibility_status=False)
	error_message=""
	if not all_slots:
		error_message="There are No cars in Parking slots"
	return render(request, 'carparking/all_slot.html',{"all_slots": all_slots,"error_message":error_message}) 

