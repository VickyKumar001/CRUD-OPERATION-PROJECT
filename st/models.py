from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.CharField(max_length=100)
    email = models.CharField(max_length=120)
    num = models.CharField(max_length=11)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)
