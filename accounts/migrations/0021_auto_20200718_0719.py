# Generated by Django 3.0.1 on 2020-07-18 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_auto_20200718_0717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='degree',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='dob',
            field=models.DateField(blank=True, help_text='yyyy-mm-dd', null=True, verbose_name='Date of Birth'),
        ),
    ]