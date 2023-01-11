from django.db import models

class Bank(models.Model):
     bankName=models.CharField(max_length=200)
     ıban=models.IntegerField(null=True)
     title=models.CharField(max_length=200)
     price=models.IntegerField()
     transactionDate=models.DateField(auto_now_add=True,null=True)
     slug=models.SlugField(unique=True,null=True)
     description=models.TextField(null=True)

class Debt(models.Model):
     namesurname=models.CharField(max_length=200)
     slug=models.SlugField(unique=True,null=True)
     price=models.IntegerField()
     debtType=models.CharField(max_length=50)
     description=models.TextField(null=True)
     date=models.DateField(auto_now_add=True,null=True)
     
