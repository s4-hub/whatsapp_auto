from django.contrib import admin
from django.urls import path, include
# from django.contrib.auth import views as auth_views

# from . import views

urlpatterns = [
    
    path('', include('components.urls')),
    path('admin/', admin.site.urls),
]
