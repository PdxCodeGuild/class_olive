# Generated by Django 4.1.1 on 2022-09-30 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groceries',
            name='created_date',
        ),
        migrations.AlterField(
            model_name='groceries',
            name='expiration_date',
            field=models.DateField(max_length=200),
        ),
    ]
