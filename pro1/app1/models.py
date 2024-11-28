from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Employee(models.Model):
    gen = [("female","female"),("male","male")]
    eid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=23)
    city = models.CharField(max_length=23)
    gender = models.CharField(max_length=23,choices=gen)
    age = models.IntegerField()
    dob = models.DateField()
    profile = models.ImageField(upload_to="profile")