# Generated by Django 3.0.1 on 2020-06-12 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0006_auto_20200609_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadsurvey',
            name='genderfilter',
            field=models.CharField(choices=[('Female', 'F'), ('Male', 'M')], default='', max_length=10),
        ),
    ]
