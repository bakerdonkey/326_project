# Generated by Django 2.1.2 on 2018-11-29 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carton', '0013_auto_20181127_0256'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='doots',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='course',
            name='updoots',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='course',
            name='rating',
            field=models.IntegerField(default=4),
        ),
    ]
