from django.contrib import admin
from .models import CustomUser
# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["username","email","last_login","age","is_staff"]
    search_fields = ['username']

admin.site.register(CustomUser,CustomUserAdmin)