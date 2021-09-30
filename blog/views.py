from django.shortcuts import render
from .models import Post,Blog


def all_blogs(request):
    posts = Post.objects.all()
    return render(request, 'blog/all_blogs.html',{'posts':posts})

def main_blog(request):
    blogs = Blog.objects.order_by('-date')[:3]
    return render(request,'blog/main_blog.html',{'blogs':blogs})
