from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=250)
    image =  models.ImageField(upload_to='blog/images/')
