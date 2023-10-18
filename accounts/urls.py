from django.urls import path
from .views import SignupView
##Write code here##
urlpatterns=[
    path('signup/',SignupView.as_view(), name= 'signup'),
]