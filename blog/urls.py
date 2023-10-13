from django.urls import path
from .views import BlogList,BlogDetail,BlogCreate
#Create your urls here
urlpatterns =[
    path('',BlogList.as_view(), name= 'blog-list'),
    path('blog/<int:pk>/',BlogDetail.as_view(), name= 'blog-detail'),
    path ('blog/create',BlogCreate.as_view(), name= 'blog-create'),
]