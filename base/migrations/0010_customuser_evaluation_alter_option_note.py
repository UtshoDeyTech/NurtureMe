# Generated by Django 4.1.7 on 2023-03-26 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_delete_generaluser'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='evaluation',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='option',
            name='note',
            field=models.CharField(default='', max_length=500),
        ),
    ]