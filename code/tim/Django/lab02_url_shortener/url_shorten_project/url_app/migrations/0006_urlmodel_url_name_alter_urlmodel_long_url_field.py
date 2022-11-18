# Generated by Django 4.1.1 on 2022-10-05 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_app', '0005_urlmodel_short_url_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='urlmodel',
            name='url_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='urlmodel',
            name='long_url_field',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
