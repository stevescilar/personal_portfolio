from django.shortcuts import render
from .models import Educ, Experience, Project, Skill

def home(request):
    projects = Project.objects.all()
    return render (request,"portfolio/home.html",{'projects':projects})
  
def home(request):
    experiences = Experience.objects.all()
    return render (request,"portfolio/home.html",{'experiences':experiences})




# def home(request):
#     skills =Skill.objects.all()
#     return render(request,"portfolio/home.html",{'skills':skills})
