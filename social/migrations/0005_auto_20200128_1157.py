# Generated by Django 3.0.2 on 2020-01-28 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0004_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='images/one.png', upload_to='images/'),
        ),
    ]