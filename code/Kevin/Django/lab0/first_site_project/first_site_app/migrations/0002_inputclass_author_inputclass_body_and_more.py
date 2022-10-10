# Generated by Django 4.1.1 on 2022-09-28 23:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_site_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inputclass',
            name='author',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='inputclass',
            name='body',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='inputclass',
            name='date_time',
            field=models.TimeField(default=datetime.datetime.now, null=True),
        ),
    ]