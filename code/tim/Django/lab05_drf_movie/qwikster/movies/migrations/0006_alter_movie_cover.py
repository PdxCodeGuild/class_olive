# Generated by Django 4.1.3 on 2022-11-22 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_alter_movie_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
