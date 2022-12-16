from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True, null=True)

class Member(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nee_name = models.CharField(max_length=50, blank=True, null=True)
    place_of_birth = models.CharField(max_length=200, blank=True)
    place_of_death = models.CharField(max_length=200, blank=True)
    date_of_birth = models.CharField(max_length=50, blank=True)
    date_of_death = models.CharField(max_length=50, blank=True)
    date_of_marriage = models.CharField(max_length=50, blank=True)
    spouses = models.ManyToManyField('self', blank=True)
    # parents = models.ManyToManyField('self', related_name=children, blank=True, symmetrical=False)
    # children = models.ManyToManyField('self', related_name=parents, blank=True, symmetrical=False)
    siblings = models.ManyToManyField('self', blank=True)
    notes = models.CharField(max_length=1000, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        if self.nee_name != None:
            return f"{self.last_name} {self.first_name}  ({self.nee_name})"
        else:
            return f"{self.last_name} {self.first_name}"

