# Generated by Django 5.0.1 on 2024-01-06 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_customuser_options_alter_customuser_managers_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membership',
            name='password',
        ),
    ]
