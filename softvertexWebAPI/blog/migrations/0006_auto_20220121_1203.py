# Generated by Django 3.2.10 on 2022-01-21 12:03

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_posted_by'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='post',
            managers=[
                ('PostsManager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='post',
            field=models.TextField(max_length=1000),
        ),
    ]
