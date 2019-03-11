from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='carparking'),
    url(
        r"^dashboard/$",views.dashboard,name="dashboard"
    ),
    url(
    	r"^get-list/$",views.get_all_slots,name="all_slots"
    )
]
