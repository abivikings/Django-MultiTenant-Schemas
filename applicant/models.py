from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    title = models.CharField(max_length=100, blank=True)
    profile_pic_url = models.TextField()
    address = models.TextField()
    about_me = models.TextField()


class Skill(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True)