from django.db import models
import time

# Create your models here.

class Parent(models.Model):
    First_Name_P = models.CharField(max_length=200)
    Last_Name_P = models.CharField(max_length=200)
    Phone_No_P = models.BigIntegerField()
    Email_ID_P= models.EmailField()
    Password_P = models.CharField(max_length=200)

class Child(models.Model):
    Parent_ID = models.ForeignKey(Parent,on_delete=models.CASCADE)
    First_Name_C = models.CharField(max_length=200)
    Last_Name_C = models.CharField(max_length=200)
    Email_ID_C = models.EmailField()
    Password_C = models.CharField(max_length=200)
    
