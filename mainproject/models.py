from django.db import models
import uuid

# Create your models here.
class Picture(models.Model):
    name = models.CharField(max_length=50, unique=True)
    picture_img = models.ImageField(upload_to='images/')
    assoc_url = models.CharField(max_length=50, default="filler")

class FilteredPicture(models.Model):
    name = models.CharField(max_length=50, unique=True)
    path = models.CharField(max_length=50, unique=True, default='filler')
    filename = models.CharField(max_length=50, unique=True, default='filler')