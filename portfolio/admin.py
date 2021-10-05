from django.contrib import admin

from .models import Educ, Experience, Project

admin.site.register(Project)

admin.site.register(Experience)

admin.site.register(Educ)