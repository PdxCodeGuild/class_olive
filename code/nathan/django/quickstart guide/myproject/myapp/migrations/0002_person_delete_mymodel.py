# Generated by Django 4.1.1 on 2022-09-28 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('height', models.CharField(max_length=4)),
                ('weight', models.CharField(max_length=4)),
            ],
        ),
        migrations.DeleteModel(
            name='MyModel',
        ),
    ]
