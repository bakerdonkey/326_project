# Generated by Django 2.1.2 on 2018-11-24 04:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carton', '0002_dootrecord_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dootrecord',
            name='course',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='courses_dooted',
        ),
        migrations.DeleteModel(
            name='DootRecord',
        ),
    ]
