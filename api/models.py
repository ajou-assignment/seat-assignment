from django.db import models
from django.db.models.fields import DecimalField

class UserSet(models.Model):
  name = models.CharField(max_length=20)
  satisfaction = models.IntegerField(null=True)

class Hist_Match(models.Model):
  stu_num1 = models.IntegerField(null=True)
  stu_num2 = models.IntegerField(null=True)
  insert_time = models.DateField(null=True)

class Satisfaction_Point(models.Model):
  stu_num_from = models.IntegerField(null=True)
  stu_num_to   = models.IntegerField(null=True)

class Student_Info(models.Model):
  stu_num    = models.IntegerField(null=True)
  stu_name   = models.CharField(max_length=50, null=True)
  stu_gender = models.CharField(max_length=10, null=True)