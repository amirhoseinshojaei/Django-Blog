from django.shortcuts import render
from django.views.generic import (ListView,DetailView)
from .models import Blog
# Create your views here.
class BlogList(ListView):
    queryset = Blog.objects.all()
    context_object_name = 'object_list'
    template_name = 'blog/blog-list.html'