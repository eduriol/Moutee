from django.db import models

class User(models.Model):
    username = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.Charfield(max_length=20)

class Guest(models.Model):
    host = models.ForeignKey(User)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
