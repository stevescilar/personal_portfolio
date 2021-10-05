from django.db import models
from django.db.models.base import Model
from django.utils.safestring import mark_safe

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/') #store in the media folder
    url = models.URLField(blank=True)

    
    def __str__(self):
        return self.title

class Experience(models.Model):
    title = models.CharField(max_length=50)
    job_description = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    duration = models.CharField(max_length=50)

    def __str__(self):
        return self.title
class Educ(models.Model):
    uni_name = models.CharField(max_length=50,help_text='Enter University name')
    study = models.CharField(max_length=100,help_text='Enter Course')
    score = models.CharField(max_length=50)
    start = models.DateField()
    complete = models.DateField()

    def __str__(self):
        return self.uni_name

class Skill(models.Model):
    skillname = models.CharField(max_length=50)
    image = models.ImageField(upload_to='portfolio/images/')
 