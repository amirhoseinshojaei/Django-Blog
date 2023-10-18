from django.shortcuts import render
from .models import CustomUser
from .forms import CustomUserCreationForm,CustomUserChangeForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
# Create your views here.
class SignupView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"