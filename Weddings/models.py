from django.db import models
from django.contrib.auth.models import User

class Wedding(models.Model):
    def __unicode__(self):
        return self.id.__str__()
    date = models.DateField()
    user1 = models.ForeignKey(User, related_name = 'wedding_from_user1')
    user2 = models.ForeignKey(User, related_name = 'wedding_from_user2')

class Guest(models.Model):
    def __unicode__(self):
        return self.id.__str__()
    wedding = models.ForeignKey(Wedding)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)