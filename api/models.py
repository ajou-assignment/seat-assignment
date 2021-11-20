from django.db import models

class Todo(models.Model):
   title = models.CharField(max_length=100)
   description = models.TextField()
   completed = models.BooleanField(default=False)

   def _str_(self):
     return self.title

class UserSet(models.Model):
  name = models.CharField(max_length=20)
  satisfaction = models.DecimalField(max_digits=8, decimal_places=2)