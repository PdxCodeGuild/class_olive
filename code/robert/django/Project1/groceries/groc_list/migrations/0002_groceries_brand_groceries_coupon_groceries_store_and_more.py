# Generated by Django 4.1.1 on 2022-09-30 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groc_list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='groceries',
            name='brand',
            field=models.CharField(default='Generic', max_length=50),
        ),
        migrations.AddField(
            model_name='groceries',
            name='coupon',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='groceries',
            name='store',
            field=models.CharField(default='S&S', max_length=50),
        ),
        migrations.AlterField(
            model_name='groceries',
            name='comp',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='groceries',
            name='item',
            field=models.CharField(default='', max_length=50),
        ),
    ]
