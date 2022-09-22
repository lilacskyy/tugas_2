from django.db import models

# Create your models here.
class MyWatchList(models.Model):
    watched = models.TextField(default='')
    title = models.TextField(default='')
    rating = models.CharField(max_length=255)
    release_date = models.CharField(max_length=30)
    review = models.TextField(default='')
