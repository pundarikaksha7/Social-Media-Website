# Generated by Django 4.0.6 on 2022-08-19 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_alter_post_caption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='caption',
            field=models.TextField(),
        ),
    ]
