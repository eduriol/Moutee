from django.db import models

class User(models.Model):
    def __unicode__(self):
        return self.username
    username = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    sex = models.BooleanField(default=True)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)

class Wedding(models.Model):
    def __unicode__(self):
        return self.id
    date = models.DateField()
    user1 = models.ForeignKey(User, related_name = 'wedding_from_user1')
    user2 = models.ForeignKey(User, related_name = 'wedding_from_user2')

class Guest(models.Model):
    def __unicode__(self):
        return self.name + ' ' + self.surname
    host = models.ForeignKey(User)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
