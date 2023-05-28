from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Appointment
import stripe
# Create your views here.


@login_required
def dashboard(request):
    if request.user.profile.role == 'doctor':
        if request.method == 'POST':
            obj_id = request.POST.get('obj_id')
            obj = Appointment.objects.get(id=obj_id)
            obj.status = request.POST.get('ac_btn')
            obj.save()
            return redirect('dashboard')
        appointment_data = Appointment.objects.filter(department=request.user.profile.department)
        context = {'role': True, 'appointment_data': appointment_data}
        return render(request, 'dashboard/doctor_dashboard.html', context)
    else:
        if request.method == 'POST':
            f_name = request.POST.get('f_name')
            l_name = request.POST.get('l_name')
            phone_num = request.POST.get('phone')
            email = request.POST.get('email')
            disease = request.POST.get('disease')
            department = request.POST.get('department')
            country = request.POST.get('country')
            city = request.POST.get('city')
            state = request.POST.get('state')
            post_code = request.POST.get('post_code')
            date = request.POST.get('date')
            time = request.POST.get('time')
            Appointment.objects.create(f_name=f_name, l_name=l_name, phone_num=phone_num, email=email,
                                       department=department, disease=disease, country=country,
                                       city=city, state=state, post_code=post_code, date=date, time=time,
                                       created_by=request.user)
            full_name = f_name + l_name
            final_price = 5
            success_url = "http://127.0.0.1:8000"
            cancel_url = "http://127.0.0.1:8000"
            stripe.api_key = 'sk_test_51NCiiREf648ZOCx8ZB0ZinGvWC8Vc6b220elROliznxvDEkGlIeuzGm06lSyxjXOqFkof2j4NwCupX5xn1gUcDu500FxzWWccc'
            lst = [({'price_data': {'currency': 'usd', 'unit_amount_decimal': final_price * 100,
                                    'product_data': {
                                        'name': full_name,
                                        'description': disease,
                                    }},
                     'quantity': 1,
                     })]
            checkout_session = stripe.checkout.Session.create(
                success_url=success_url,
                cancel_url=cancel_url,
                payment_method_types=['card'],
                mode='payment',
                line_items=lst,
            )
            return redirect(checkout_session.url)
        appointment_data = Appointment.objects.filter(created_by=request.user)
        context = {'role': False, 'appointment_data': appointment_data}
        return render(request, 'dashboard/patient-dashboard.html', context)
