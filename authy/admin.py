from django.contrib import admin
from authy.models import UserProfile


class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'country', 'role')


admin.site.register(UserProfile, UserAdmin)


# Register your models here.
