# Generated by Django 3.2.7 on 2021-09-14 08:31

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_name', models.CharField(max_length=50, null=True)),
                ('org_short_name', models.CharField(max_length=50, null=True)),
                ('org_location', models.CharField(max_length=100, null=True)),
                ('org_logo_dir', models.TextField()),
                ('org_admin_name', models.CharField(max_length=50, null=True)),
                ('user_ing_url', models.TextField()),
                ('org_admin_email', models.EmailField(max_length=50, unique=True, validators=[django.core.validators.EmailValidator()])),
                ('password', models.TextField()),
                ('role_id', models.ImageField(upload_to='')),
                ('role_name', models.CharField(max_length=50)),
                ('is_approved', models.BooleanField(default=False)),
                ('created_on', models.DateField(default=datetime.datetime.now)),
            ],
        ),
    ]