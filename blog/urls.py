from django.urls import path
from .views import BlogList,BlogDetail,BlogCreate,BlogUpdate,BlogDelete
#Create your urls here
urlpatterns =[
    path('',BlogList.as_view(), name= 'blog-list'),
    path('blog/<int:pk>/',BlogDetail.as_view(), name= 'blog-detail'),
    path ('blog/create',BlogCreate.as_view(), name= 'blog-create'),
    path ('blog/<int:pk>/update', BlogUpdate.as_view(), name='blog-update'),
    path ('blog/<int:pk>/delet',BlogDelete.as_view(), name= 'blog-delet'),
]