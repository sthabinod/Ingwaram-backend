# Generated by Django 3.2.7 on 2021-12-18 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_event_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('sub_title', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Events',
            },
        ),
    ]
