# Generated by Django 3.0.6 on 2020-05-20 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20200520_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.TextField(null=True),
        ),
    ]
