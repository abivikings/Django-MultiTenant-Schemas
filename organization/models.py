from datetime import datetime

from django.core.validators import validate_email
from django.db import models


class Role(models.Model):
    role_name = models.CharField(max_length=50)


class Users(models.Model):
    org_name = models.CharField(max_length=50, null=True)
    org_short_name = models.CharField(max_length=50, null=True)
    org_location = models.CharField(max_length=100, null=True)
    org_logo_dir = models.TextField()

    org_admin_name = models.CharField(max_length=50, null=True)
    user_ing_url = models.TextField()
    org_admin_email = models.EmailField(max_length=50, unique=True, blank=False, validators=[validate_email])
    password = models.TextField()
    role_id = models.ImageField()
    role_name = models.CharField(max_length=50)
    is_approved = models.BooleanField(default=False)
    created_on = models.DateField(default=datetime.now)