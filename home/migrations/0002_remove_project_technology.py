# Generated by Django 3.1.1 on 2020-09-30 03:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='technology',
        ),
    ]
