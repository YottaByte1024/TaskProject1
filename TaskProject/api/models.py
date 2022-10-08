from django.db import models


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

    @property
    def dep_current(self):
        from django.utils import timezone
        now = timezone.now()

        if self.date_transfer is None:
            current_dep = self.id_dep_new_id
        elif self.date_transfer <= now:
            current_dep = self.id_dep_new_id
        else:
            current_dep = self.id_dep_old_id

        return current_dep

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

    @property
    def employees_current(self):
        return self.dep_new.filter()

    def __str__(self):
        return "%s %s" % (self.name, self.isWorking)
