from django.shortcuts import render
from .models import Educ, Experience, Project

def home(request):
    projects = Project.objects.all()
    return render (request,"portfolio/home.html",{'projects':projects})

def home(request):
    experiences = Experience.objects.all()
    return render (request,"portfolio/home.html",{'experiences':experiences})

def home(request):
    educs = Educ.objects.all()
    return render (request,"portfolio/home.html",{'educs':educs})
