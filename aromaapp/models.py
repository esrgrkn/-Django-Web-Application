from django.db import models
from uuid import uuid1
from django.utils.text import slugify
from datetime import datetime,date

PRICE=[
     ('1','1'),
     ('2','2'),
     ('3','3'),
     ('4','4'),
     ('5','5'),
     ('6','6'),
     ('7','7'),
     ('8','8'),
     ('9','9'),
     ('9','9'),
]

class CustomersTable(models.Model):
     slug=models.SlugField(null=False,unique=True,db_index=True) 
     namesurname=models.CharField(max_length=20)
     tc=models.IntegerField(blank=True)
     phoneNum=models.IntegerField(blank=False)
     customerImage=models.ImageField(upload_to="uploads",null=True,default="")  
     date=models.DateField(auto_now_add=True,blank=True)
     def __str__(self):
      return f"{self.date.strftime('%d-%m-%Y')}"
     def __str__(self): 
          return f" Adı Soyafdı:{self.namesurname}-Tc numarası{self.tc}"
     def save(self,*args,**kwargs):
          self.slug=slugify(self.namesurname)
          super().save(*args,**kwargs)
     

class ProductTable(models.Model):
     
     namesurname=models.CharField(max_length=20)
     slug=models.SlugField(null=False,unique=False,blank=True,db_index=True) 
     adet=models.IntegerField(default="",blank=False)
     daralı=models.IntegerField(default="",blank=False)
     safi=models.IntegerField(default="")
     tutar=models.IntegerField(default="")
     date=models.DateField(auto_now_add=True,blank=True)
     def __str__(self):
      return f"{self.date.strftime('%d-%m-%Y')}"
     def save(self,*args,**kwargs):
          self.slug=slugify(self.namesurname)
          super().save(*args,**kwargs)

class Price(models.Model):
     price=models.FloatField()

class Kilogram(models.Model):
     kilo=models.FloatField()

class Company(models.Model):
     company=models.CharField(max_length=100)

class Paids(models.Model):
     namesurname=models.CharField(max_length=20)
     adet=models.IntegerField(default="",blank=False)
     daralı=models.IntegerField(default="",blank=False)
     safi=models.IntegerField(default="")
     tutar=models.IntegerField(default="")
     date=models.DateField(auto_now_add=True,blank=True)
     
    
