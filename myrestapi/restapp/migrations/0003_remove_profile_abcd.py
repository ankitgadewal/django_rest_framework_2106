# Generated by Django 3.0.8 on 2020-07-07 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0002_profile_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='abcd',
        ),
    ]
