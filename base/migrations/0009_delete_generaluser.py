# Generated by Django 4.1.7 on 2023-03-23 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='GeneralUser',
        ),
    ]
