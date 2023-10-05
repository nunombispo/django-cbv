from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView

from .forms import BlogForm
from .models import Blog


class BlogListView(ListView):
    model = Blog
    template_name = 'blog_list.html'
    context_object_name = 'blogs'


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'
    context_object_name = 'blog'


class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForm
    template_name = 'blog_create.html'
    success_url = reverse_lazy('blog_list')


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog_delete.html'
    success_url = reverse_lazy('blog_list')
