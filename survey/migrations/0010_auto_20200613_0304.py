# Generated by Django 3.0.1 on 2020-06-13 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0009_auto_20200613_0246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadsurvey',
            name='gender_filter',
        ),
        migrations.AddField(
            model_name='uploadsurvey',
            name='gender_filter',
            field=models.ManyToManyField(blank=True, null=True, to='survey.GenderFilter'),
        ),
    ]