# Generated by Django 5.0.8 on 2024-08-20 04:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0015_alter_project_shared_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='project',
        ),
    ]
