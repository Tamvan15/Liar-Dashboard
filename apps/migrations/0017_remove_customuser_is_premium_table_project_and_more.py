# Generated by Django 5.1 on 2024-08-20 04:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0016_remove_table_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_premium',
        ),
        migrations.AddField(
            model_name='table',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tables', to='apps.project'),
        ),
        migrations.AlterField(
            model_name='project',
            name='shared_users',
            field=models.ManyToManyField(blank=True, related_name='shared_projects', to=settings.AUTH_USER_MODEL),
        ),
    ]
