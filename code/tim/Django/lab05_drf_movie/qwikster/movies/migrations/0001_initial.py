# Generated by Django 4.1.3 on 2022-11-23 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=200)),
                ('year', models.CharField(max_length=4)),
                ('metacritic', models.CharField(max_length=200)),
            ],
        ),
    ]