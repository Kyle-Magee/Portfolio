from django.contrib import admin
from .models import UserInformation, Roles

# Register your models here.
admin.site.register(UserInformation)
admin.site.register(Roles)