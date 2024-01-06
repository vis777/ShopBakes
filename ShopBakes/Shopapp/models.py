from django.db import models

# Create your models here.
class CategoryDb(models.Model):
    Category_Name = models.CharField(max_length=100, null=True, blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)
    Category_Image = models.ImageField(upload_to="Categoryimage", null=True, blank=True)
class ProductDb(models.Model):
    Product_Category = models.CharField(max_length=100, null=True, blank=True)
    Product_Name = models.CharField(max_length=100, null=True, blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)
    Product_Price = models.IntegerField(null=True, blank=True)
    Product_Image = models.ImageField(upload_to="Productimage", null=True, blank=True)
