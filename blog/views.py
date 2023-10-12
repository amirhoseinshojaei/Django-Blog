from django.shortcuts import render
from django.views.generic import (ListView,DetailView,CreateView)
from .models import Blog
from django.views.generic.edit import UpdateView,DeleteView
# Create your views here.
class BlogList(ListView):
    queryset = Blog.objects.all()
    context_object_name = 'object_list'
    template_name = 'blog/blog-list.html'

class BlogDetail(DetailView):
    model = Blog
    context_object_name = 'objects'
    template_name = 'blog/blog-detail.html'

class BlogCreate(CreateView):
    model = Blog
    fields = ['title','description','author']
    context_object_name = 'objects-create'
    template_name = 'blog/blog-create.html'
    # To do : complete security