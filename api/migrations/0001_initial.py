# Generated by Django 3.0.14 on 2021-12-07 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hist_Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_num1', models.IntegerField(null=True)),
                ('stu_num2', models.IntegerField(null=True)),
                ('insert_time', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Satisfaction_Point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_num_from', models.IntegerField(null=True)),
                ('stu_num_to', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_num', models.IntegerField(null=True)),
                ('stu_name', models.CharField(max_length=50, null=True)),
                ('stu_gender', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('satisfaction', models.IntegerField(null=True)),
            ],
        ),
    ]
