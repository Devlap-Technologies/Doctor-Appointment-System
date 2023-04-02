from django.db import models
from django.contrib.auth.models import User

ROLE_STATUS = [('doctor', 'doctor'),
               ('patient', 'patient')]


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    profile_photo = models.ImageField(upload_to='profile_photo/', blank=True, null=True)
    phone_number = models.BigIntegerField(default=0, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    zip_code = models.CharField(max_length=255, blank=True, null=True)
    role = models.CharField(max_length=255,  choices=ROLE_STATUS, default='doctor')

    @property
    def useremail(self):
        return self.user.email
