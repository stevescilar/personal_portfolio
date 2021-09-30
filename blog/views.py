from django.shortcuts import render , get_object_or_404
from .models import Post,Blog


def all_blogs(request):
    posts = Post.objects.all()
    return render(request, 'blog/all_blogs.html',{'posts':posts})

def main_blog(request):
    blogs = Blog.objects.order_by('-date')
    return render(request,'blog/main_blog.html',{'blogs':blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html',{'blog':blog})
