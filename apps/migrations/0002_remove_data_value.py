# Generated by Django 5.0.6 on 2024-08-15 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='value',
        ),
    ]
