# Generated by Django 3.0.1 on 2020-07-18 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_auto_20200718_0557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='profile_pic',
            field=models.ImageField(upload_to='profile_pics'),
        ),
    ]
