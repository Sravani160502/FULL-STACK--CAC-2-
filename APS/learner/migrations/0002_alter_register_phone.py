# Generated by Django 4.2.7 on 2024-01-25 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
