from django import forms
from django.contrib.auth.forms import (UserCreationForm,UserChangeForm)
from .models import CustomUser
# Write Code here
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields+('age','email')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields