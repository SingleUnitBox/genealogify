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
    spouses = models.ManyToManyField('self', related_name="rel_spouses", blank=True, symmetrical=False)
    parents = models.ManyToManyField('self', related_name="rel_children", blank=True, symmetrical=False, null=True)
    children = models.ManyToManyField('self', related_name="rel_parents", blank=True, symmetrical=False, null=True)
    siblings = models.ManyToManyField('self', related_name="rel_siblings", blank=True, symmetrical=False, null=True)
    notes = models.CharField(max_length=1000, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        if self.nee_name == "":
            return f"{self.last_name} {self.first_name}"
        else:
            return f"{self.last_name} {self.first_name}  ({self.nee_name})"

