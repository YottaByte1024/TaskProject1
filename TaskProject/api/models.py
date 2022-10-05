from django.db import models
from datetime import datetime


# Create your models here.

class Employee(models.Model):
    lastname = models.CharField(max_length=40)
    firstname = models.CharField(max_length=40)
    patronymic = models.CharField(max_length=40, blank=True)
    id_dep_old = models.ForeignKey('Dep', related_name='dep_old',
                                   null=True, blank=True, on_delete=models.SET_NULL)
    id_dep_new = models.ForeignKey('Dep', related_name='dep_new',
                                   null=True, blank=True, on_delete=models.SET_NULL)
    date_transfer = models.DateTimeField(null=True, blank=True)
    date_create = models.DateTimeField(auto_now_add=True)
    date_change = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s %s" % (self.lastname, self.firstname)


class Dep(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=128)
    id_head = models.ForeignKey(Employee,
                                null=True, blank=True, on_delete=models.SET_NULL)
    isWorking = models.BooleanField(default=True)
    date_create = models.DateTimeField(auto_now_add=True)
    date_change = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s %s" % (self.name, self.isWorking)