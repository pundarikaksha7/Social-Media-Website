# Generated by Django 4.0.6 on 2022-08-19 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_remove_post_likes_post_favourites'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='caption',
            field=models.TextField(default='Bio'),
        ),
    ]
