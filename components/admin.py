from django.contrib import admin
from .models import Messages, Profile

# Register your models here.
admin.site.register(Messages)
admin.site.register(Profile)