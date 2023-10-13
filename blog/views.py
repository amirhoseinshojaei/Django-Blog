from django.shortcuts import render
from django.views.generic import (ListView,DetailView,CreateView)
from .models import Blog
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse,reverse_lazy
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
    success_url = reverse_lazy ('blog-list')

class BlogUpdate(UpdateView):
    model = Blog
    fields = ['title','description','author']
    context_object_name = 'objects-update'
    template_name = 'blog/blog-update.html'
    success_url = reverse_lazy ('blog-list')

class BlogDelete(DeleteView):
    model = Blog
    success_url = reverse_lazy ('blog-list')
    template_name = 'blog/blog-delet.html'
    

