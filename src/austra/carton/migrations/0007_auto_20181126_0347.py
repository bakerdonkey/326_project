# Generated by Django 2.1.2 on 2018-11-26 03:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carton', '0006_auto_20181126_0044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='courses_past',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sessions_current',
        ),
    ]