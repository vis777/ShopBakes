from django.db import models

# Create your models here.
class ContactDb(models.Model):
    Contact_Name = models.CharField(max_length=100, null=True, blank=True)
    Contact_Email = models.CharField(max_length=100, null=True, blank=True)
    Subject = models.CharField(max_length=100, null=True, blank=True)
    Message = models.CharField(max_length=100, null=True, blank=True)
class RegisterDb(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Mobile_Number =  models.IntegerField(null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)
    UserName = models.CharField(max_length=100, null=True, blank=True)
    PassWord = models.CharField(max_length=100, null=True, blank=True)
class CartDb(models.Model):
    Username = models.CharField(max_length=100, null=True, blank=True)
    Productname = models.CharField(max_length=100, null=True, blank=True)
    Quantity = models.IntegerField(null=True, blank=True)
    Total_Price = models.IntegerField(null=True, blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)
class Checkoutdb(models.Model):
    FirstName=models.CharField(max_length=100,null=True,blank=True)
    LastName=models.CharField(max_length=100,null=True,blank=True)
    EmailId = models.CharField(max_length=100, null=True, blank=True)
    Address = models.CharField(max_length=100, null=True, blank=True)
    City=models.CharField(max_length=100,null=True,blank=True)
    Country=models.CharField(max_length=100,null=True,blank=True)
    Telephone=models.IntegerField(null=True,blank=True)
