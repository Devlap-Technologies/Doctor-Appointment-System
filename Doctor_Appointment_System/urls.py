from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('dasboard/', include('dashboard.urls')),
    path('auth/', include('authy.urls')),
]
