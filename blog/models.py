from django.db import models


# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=50, default='')
    desc = models.CharField(max_length=100, default='')