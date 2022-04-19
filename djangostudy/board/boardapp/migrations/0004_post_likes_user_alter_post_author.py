# Generated by Django 4.0.4 on 2022-04-19 06:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('boardapp', '0003_comment_author_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes_user',
            field=models.ManyToManyField(related_name='likes_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_post', to=settings.AUTH_USER_MODEL),
        ),
    ]