# Generated by Django 3.2.7 on 2021-12-19 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_event_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='category',
        ),
    ]
