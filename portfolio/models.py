from django.db import models
from django.db.models.base import Model

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

class Educ(models.Model):
    uni_name = models.CharField(max_length=50)
    study = models.CharField(max_length=100)
    score = models.CharField(max_length=50)
    start = models.DateField()
    complete = models.DateField()

