# Generated by Django 5.0.3 on 2024-04-01 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Portal_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='full_name',
        ),
    ]
