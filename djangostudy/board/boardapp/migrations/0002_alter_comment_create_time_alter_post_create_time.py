# Generated by Django 4.0.4 on 2022-04-12 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
