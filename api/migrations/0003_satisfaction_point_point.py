# Generated by Django 3.0.14 on 2021-12-07 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_hist_match_insert_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='satisfaction_point',
            name='point',
            field=models.IntegerField(null=True),
        ),
    ]
