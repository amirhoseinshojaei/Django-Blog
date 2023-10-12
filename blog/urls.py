from django.urls import path
from .views import BlogList,BlogDetail
#Create your urls here
urlpatterns =[
    path('',BlogList.as_view(), name= 'blog-list'),
    path('blog/<int:pk>/',BlogDetail.as_view(), name= 'blog-detail'),
]