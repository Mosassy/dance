from django.db import models
from django.contrib.auth.models import User


class StudentIntakeForm(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    cel_phone = models.IntegerField()
    texts_ok = bool
    first_name_of_student = models.CharField(max_length=50)
    class_interest = models.TextField()
    previous_experience = bool
    number_of_years = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.last_name


class Parent(User):
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip = models.IntegerField()
    cel_phone = models.IntegerField()
    home_phone = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.last_name