# Generated by Django 4.0.4 on 2022-04-19 06:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('boardapp', '0004_post_likes_user_alter_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='likes_user',
            field=models.ManyToManyField(related_name='comment_likes_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_comment', to=settings.AUTH_USER_MODEL),
        ),
    ]