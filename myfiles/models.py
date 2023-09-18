from django.db import models

# Create your models here.
class Subscribe(models.Model):
    ism = models.CharField(max_length=30)
    fam = models.CharField(max_length=30,null=True,blank=True)
    username = models.CharField(max_length=30,null=True,blank=True)
    tg_id = models.IntegerField(unique=True)
class Menu(models.Model):
    nomi = models.CharField(max_length=30)

class Maxsulotlar(models.Model):
    nomi = models.CharField(max_length=30)
    narxi = models.IntegerField(unique=True)
    rasm = models.CharField(max_length=300)
    malumot = models.CharField(max_length=30, null=True, blank=True)
    turi = models.CharField(max_length=30)

class Korzinka(models.Model):
    nomi = models.CharField(max_length=30)
    narxi = models.IntegerField()
    rasm = models.CharField(max_length=300)
    malumot = models.CharField(max_length=30, null=True, blank=True)
    turi = models.CharField(max_length=30)
    soni = models.IntegerField()
    tg_id = models.IntegerField()
    username = models.CharField(max_length=30,null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
