from .views import *
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('', login_view, name='login'),
    path('/', profile_view, name='profile'),
    path('logprofileout/', logout_user, name='logout'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
         activate, name='activate'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="login/forget-password.html",
                                                                 html_email_template_name='login/forgot_mail.html'),
         name="reset_password"),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="login/passwordsent.html"),
         name="password_reset_done"),

        path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
            template_name="login/changepassword.html"), name="password_reset_confirm"),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="login/restdone.html"),
         name="password_reset_complete"),
]
