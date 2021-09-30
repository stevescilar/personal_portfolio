from django.contrib import admin
from django.urls import path
from . import views

app_name = 'blog'


urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('', views.all_blogs, name='all_blogs'),
    path('', views.main_blog, name='main_blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
]