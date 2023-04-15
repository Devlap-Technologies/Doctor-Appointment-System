from django.urls import path
from .views import index
from .views import *
urlpatterns = [
    path('', index, name='home'),
    path('about',about,name='about'),
    path('service',services,name='services'),
    path('appoinment', appoinment,name='appoinment'),
    path('contact', contact, name='contact'),
    path('doctor',doctor,name='doctor'),
    path('doctor-single',doctor_single,name='doctor_single')

]
