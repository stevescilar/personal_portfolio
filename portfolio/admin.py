from django.contrib import admin

from .models import Educ, Experience, Project, Skill

admin.site.register(Project)

admin.site.register(Experience)

admin.site.register(Educ)

admin.site.register(Skill)

class  authorAdmin(admin.ModelAdmin):
    list_display=['name','image_tag']