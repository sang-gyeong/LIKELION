# Generated by Django 3.0.6 on 2020-05-18 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200516_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date_time',
            field=models.CharField(max_length=200),
        ),
    ]
