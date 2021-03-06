# Generated by Django 3.2.7 on 2021-12-19 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('father', models.CharField(max_length=200)),
                ('mother', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images')),
            ],
            options={
                'verbose_name_plural': 'Writer',
            },
        ),
    ]
