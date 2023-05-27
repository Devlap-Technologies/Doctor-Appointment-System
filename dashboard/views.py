from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def dashboard(request):
    if request.user.profile.role == 'doctor':
        context = {'role': True}
        return render(request, 'dashboard/doctor_dashboard.html', context)
    else:
        context = {'role': False}
        return render(request, 'dashboard/patient-dashboard.html', context)
