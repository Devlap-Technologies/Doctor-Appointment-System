from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Appointment(models.Model):
    f_name = models.CharField(max_length=100, blank=True, null=True)
    l_name = models.CharField(max_length=100, blank=True, null=True)
    phone_num = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    disease = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    post_code = models.CharField(max_length=100, blank=True, null=True)
    date = models.CharField(max_length=100, blank=True, null=True)
    time = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=25, default='Pending')

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.f_name

