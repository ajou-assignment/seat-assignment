# Generated by Django 3.0.14 on 2021-12-07 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hist_match',
            name='insert_time',
        ),
    ]