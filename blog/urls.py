from django.urls import path
from .views import BlogList
#Create your urls here
urlpatterns =[
    path('',BlogList.as_view(), name= 'blog-list')
]