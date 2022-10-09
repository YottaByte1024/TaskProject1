from django.db import models


# Create your models here.

class Employee(models.Model):
    lastname = models.CharField(max_length=40)
    firstname = models.CharField(max_length=40)
    patronymic = models.CharField(max_length=40, blank=True)
    date_create = models.DateTimeField(auto_now_add=True)
    date_change = models.DateTimeField(auto_now=True)

    @property
    def transfer_current(self):
        from django.utils import timezone
        now = timezone.now()
        transfer = self.transfers.filter(date_transfer__lte=now) \
            .order_by('date_transfer').last()
        if transfer is None:
            return None
        return transfer.id

    @property
    def dep_current(self):
        from django.utils import timezone
        now = timezone.now()
        dep = self.transfers.filter(date_transfer__lte=now) \
            .order_by('date_transfer').last()
        if dep is None:
            return None
        return dep.dep.code

    def __str__(self):
        return "%s %s %s from %s" % (self.lastname, self.firstname, self.patronymic,
                                     self.dep_current)

    class Meta:
        verbose_name = 'employee'
        verbose_name_plural = 'employees'


class Dep(models.Model):
    # id = models.CharField(max_length=10, primary_key=True)
    code = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=128)
    head = models.ForeignKey(Employee, related_name='managed_dep',
                             null=True, blank=True, on_delete=models.SET_NULL)
    is_working = models.BooleanField(default=True)
    date_create = models.DateTimeField(auto_now_add=True)
    date_change = models.DateTimeField(auto_now=True)

    def __str__(self):
        match self.is_working:
            case True:
                w = 'is working'
            case _:
                w = 'is not working'
        return "%s (%s) %s" % (self.name, self.code, w)

    class Meta:
        verbose_name = 'dep'
        verbose_name_plural = 'deps'


class Transfer(models.Model):
    employee = models.ForeignKey(Employee, related_name='transfers',
                                 null=True, blank=True, on_delete=models.SET_NULL)
    dep = models.ForeignKey(Dep, related_name='transfers',
                            null=True, blank=True, on_delete=models.SET_NULL)
    date_transfer = models.DateTimeField()
    date_create = models.DateTimeField(auto_now_add=True)
    date_change = models.DateTimeField(auto_now=True)

    def __str__(self):
        from django.utils import timezone
        tz = timezone.get_default_timezone()
        return "%s is transferred to %s at %s" % (
            self.employee, self.dep.name,
            self.date_transfer.astimezone(tz).strftime('%d.%m.%Y %H:%M'))

    class Meta:
        verbose_name = 'transfer'
        verbose_name_plural = 'transfers'
