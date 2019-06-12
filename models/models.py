from django.db import models
from django.utils.timezone import now
# Create your models here.

class Customer_Recipes(models.Model):
      id  = models.AutoField(primary_key=True)
      pid = models.IntegerField(blank=False)
      recipeid = models.IntegerField(blank=False)
       
class Customer_Restrictions(models.Model):
    id  = models.AutoField(primary_key=True)
    pid = models.IntegerField(blank=False)
    dietid = models.IntegerField(blank=False)

class UserType(models.Model):
    id  = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

class User(models.Model):
    id  = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    secret = models.CharField(max_length=200)
    usertype = models.IntegerField(blank=False)
    createdate = models.DateField(default=now)

class Profile(models.Model):
      id         = models.AutoField(primary_key=True)
      uid        = models.IntegerField(blank=False, null=False)
      firstname  = models.CharField(max_length=100)
      lastname   = models.CharField(max_length=100)
      email      = models.EmailField(max_length=100,blank=False, null=False)
      telephone  = models.CharField(max_length=30)
      address    = models.CharField(max_length=100)
      address2   = models.CharField(max_length=100)
      zipcode    = models.CharField(max_length=15)
      state      = models.CharField(max_length=2)
      createdate = models.DateTimeField(default=now)
    
class Deliveries(models.Model):
    id  = models.AutoField(primary_key=True)
    vendor = models.CharField(max_length=500)
    receivedate = models.DateField(default=now)

class Delivery_Quantities(models.Model):
    id         = models.AutoField(primary_key=True)
    productid  = models.IntegerField(blank=False, null=False)
    qty        = models.IntegerField(blank=False, null=False)
    deliveryid = models.IntegerField(blank=False, null=False) 
    
class Dietary_Restrictions(models.Model):
      id    = models.AutoField(primary_key=True)
      name  = models.CharField(max_length=100,blank=False, null=False)
      
class Icon(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=500,blank=False, null=False)
    credit = models.CharField(max_length=100,blank=False, null=False)
   
class Order_Quantities(models.Model):
    id         = models.AutoField(primary_key=True)
    productid  = models.IntegerField(blank=False, null=False)
    qty        = models.IntegerField(blank=False, null=False)
    orderid = models.IntegerField(blank=False, null=False) 
    
class Orders(models.Model):
    id         = models.AutoField(primary_key=True)
    uid        = models.IntegerField(blank=False, null=False)
    placedate  = models.DateField(default=now)
    total      = models.IntegerField()
    pickupid   = models.IntegerField(blank=False, null=False)
    recieved_at = models.DateField() 

class Pick(models.Model):
      id         = models.AutoField(primary_key=True)
      name       = models.CharField(max_length=100)
      address    = models.CharField(max_length=100,blank=False, null=False)
      description = models.CharField(max_length=100)
      zipcode    = models.CharField(max_length=15)
      state      = models.CharField(max_length=2)

class ProductTags(models.Model):
      id         = models.AutoField(primary_key=True)
      productid  = models.IntegerField(blank=False, null=False)
      tagid      = models.IntegerField(blank=False, null=False)

class Tags(models.Model):
     id = models.AutoField(primary_key=True)
     name =  models.CharField(max_length=100)

class Recipes(models.Model):
     id = models.AutoField(primary_key=True)
     url =  models.CharField(max_length=100,blank=False, null=False)
     name =  models.CharField(max_length=100,blank=False, null=False)
     ingredients =models.TextField()
     img = models.CharField(max_length=300)

class Product(models.Model):
      id         = models.AutoField(primary_key=True)
      name       = models.CharField(max_length=200,blank=False, null=False)
      description =  models.TextField()
      weight     = models.FloatField()
      unit   = models.CharField(max_length=30)
      price  = models.FloatField()
      priceper = models.IntegerField()
      perunit = models.CharField(max_length=50)
      aisle   = models.CharField(max_length=50)
      category   = models.CharField(max_length=50)
      img   = models.CharField(max_length=500)
      iconid = models.IntegerField()
      color  = models.CharField(max_length=10)
      searchitem   = models.CharField(max_length=50)
      searchstrength = models.IntegerField()
      
      
     

