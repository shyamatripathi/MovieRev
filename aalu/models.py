from django.db import models

# Create your models here.
class Login(models.Model):
    name=models.CharField(max_length=10)
    password=models.TextField(max_length=33)


class Signin(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
  

class Review1(models.Model):
    search=models.CharField(max_length=10)

class UserRev(models.Model):
    name = models.CharField(max_length=100)
    movie = models.CharField(max_length=100)
    review = models.CharField(max_length=100)
    