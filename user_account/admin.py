from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user_account.models import CustomUser
admin.site.register(CustomUser,UserAdmin)