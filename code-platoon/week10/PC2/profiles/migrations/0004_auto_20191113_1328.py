# Generated by Django 2.2.7 on 2019-11-13 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20191113_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet_profile',
            name='age',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='user_age',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='zip',
            field=models.CharField(max_length=20),
        ),
    ]