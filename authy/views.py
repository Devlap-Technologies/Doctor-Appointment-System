from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .token import account_activation_token
from django.contrib.auth.models import User, auth
from django.core.mail import EmailMessage
from .models import UserProfile
from django.contrib.auth.decorators import login_required
import threading


class EmailThread(threading.Thread):

    def __init__(self, emails):
        self.emails = emails
        threading.Thread.__init__(self)

    def run(self) -> None:
        self.emails.send(fail_silently=False)


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        country = request.POST.get('country')
        zip_code = request.POST.get('zip_code')
        role = request.POST.get('role')
        profile_photo = request.POST.get('profile_photo')
        user = User(username=username, email=email)
        user.is_active = False
        user.set_password(password)
        user.save()
        user_profile = UserProfile(user=user, first_name=first_name, last_name=last_name, phone_number=phone_number,
                                   country=country, zip_code=zip_code, role=role, profile_photo=profile_photo)
        user_profile.save()
        current_site = get_current_site(request)
        mail_subject = 'Activate your account.'
        html_template = 'account_activation_mail.html'
        message = render_to_string(html_template, {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        email = EmailMessage(
                    mail_subject, message, to=[email]
        )
        email.content_subtype = 'html'
        EmailThread(email).start()
        return render(request, 'email_sent.html')
    return render(request, 'register.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return HttpResponse('Activation link is invalid!')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = auth.authenticate(email=email, password=password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    if user.profile.role == 'doctor':
                        return redirect('/api/admin/')
                    else:
                        return redirect('/')
                else:
                    msg = 'Your Email is not Verify Please Check Your Email First'
                    return render(request, 'loginpage.html', {'msg': msg})
            else:
                msg = 'Username or Password Incorrect'
                return render(request, 'loginpage.html', {'msg': msg})
    return render(request, 'loginpage.html')


@login_required()
def profile_view(request):
    user = request.user
    user_data = UserProfile.objects.get(user=user)
    context = {'user_data': user_data}
    return render(request, 'app-profile.html', context)


def logout_user(request):
    auth.logout(request)
    return redirect('login')
