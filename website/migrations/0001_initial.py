# Generated by Django 3.2.7 on 2021-12-17 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('organiser', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name_plural': 'Events',
            },
        ),
    ]
