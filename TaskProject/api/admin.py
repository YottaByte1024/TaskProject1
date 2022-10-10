from django.contrib import admin
from .models import Employee, Dep, Transfer, Appointment

# Register your models here.
admin.site.register(Employee)
admin.site.register(Dep)
admin.site.register(Transfer)
admin.site.register(Appointment)
