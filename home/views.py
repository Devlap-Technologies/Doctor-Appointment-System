from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
def services(request):
    return render(request, 'service.html')

def appoinment(request):
    return render(request, 'appoinment.html')

def contact(request):
    return render(request, 'contact.html')
def doctor(request):
    return render(request,'doctor.html')
def doctor_single(request):
    return render(request,'doctor-single.html')