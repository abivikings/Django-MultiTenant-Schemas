from django.core.validators import validate_email
from django.db import models
from django.utils.datetime_safe import datetime
from django_tenants.models import TenantMixin, DomainMixin
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class Organization(TenantMixin):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, blank=False, unique=True, validators=[validate_email])
    phone = models.CharField(max_length=50, unique=True, null=False)
    created_on = models.DateField(default=datetime.now, blank=True)

    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True

    def __str__(self):
        return self.name


class Domain(DomainMixin):
    def __str__(self):
        return self.domain


class OrgTemp(models.Model):
    type = models.CharField(max_length=50, blank=False)
    org_name = models.CharField(max_length=100, blank=False)
    org_email = models.EmailField(max_length=254, blank=False, unique=True, validators=[validate_email])
    org_phone = models.TextField(blank=False, unique=True)
    is_approved = models.BooleanField(default=False)