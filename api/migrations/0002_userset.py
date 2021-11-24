# Generated by Django 2.1.15 on 2021-11-19 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('satisfaction', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
    ]