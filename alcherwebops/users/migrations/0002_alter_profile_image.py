# Generated by Django 4.0.6 on 2022-08-18 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default1.png', upload_to='profile_pics'),
        ),
    ]
