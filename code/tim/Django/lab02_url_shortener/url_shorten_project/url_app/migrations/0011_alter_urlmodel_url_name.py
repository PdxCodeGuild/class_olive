# Generated by Django 4.1.1 on 2022-10-06 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_app', '0010_urlmodel_url_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlmodel',
            name='url_name',
            field=models.URLField(null=True),
        ),
    ]
