from django.db import models

# Create your models here.

class PemainBola(models.Model):
    nama = models.CharField(max_length=100)
    id   = models.CharField(max_length=4, unique=True, primary_key=True) # fungsi untuk biar tidak ada id duplikat
    domisili = models.CharField(max_length=50)
    tanggalLahir = models.DateField(null=True, blank=True) 

def __str__(self):
        return f"{self.nama} - {self.id}"

class Klub(models.Model):
      nama = models.CharField(max_length=100)
      negara = models.CharField(max_length=100)
      tahunberdiri = models.IntegerField()

def __str__(self):
      return self.nama