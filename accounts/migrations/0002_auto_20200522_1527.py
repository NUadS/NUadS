# Generated by Django 3.0.6 on 2020-05-22 07:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='dob',
            field=models.DateField(default=datetime.date.today, verbose_name='Date of Birth'),
        ),
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='student',
            name='year_in_school',
            field=models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior'), ('GR', 'Graduate')], default='FR', max_length=2),
        ),
        migrations.AlterField(
            model_name='degree',
            name='minor',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.TextField(choices=[('F', 'F'), ('M', 'M')], max_length=1),
        ),
    ]