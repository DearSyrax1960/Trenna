# Generated by Django 5.0.6 on 2024-05-30 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='workspace',
            name='slug',
        ),
    ]