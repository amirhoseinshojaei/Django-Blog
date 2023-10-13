from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import (ListView,DetailView,CreateView)
from .models import Blog
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse,reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# Create your views here.
class BlogList(ListView):
    queryset = Blog.objects.all()
    context_object_name = 'object_list'
    template_name = 'blog/blog-list.html'

class BlogDetail(LoginRequiredMixin,DetailView):
    model = Blog
    context_object_name = 'objects'
    template_name = 'blog/blog-detail.html'

class BlogCreate(LoginRequiredMixin,CreateView):
    model = Blog
    fields = ['title','description']
    context_object_name = 'objects-create'
    template_name = 'blog/blog-create.html'
    success_url = reverse_lazy ('blog-list')

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogUpdate(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Blog
    fields = ['title','description']
    context_object_name = 'objects-update'
    template_name = 'blog/blog-update.html'
    success_url = reverse_lazy ('blog-list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class BlogDelete(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Blog
    success_url = reverse_lazy ('blog-list')
    template_name = 'blog/blog-delet.html'
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

