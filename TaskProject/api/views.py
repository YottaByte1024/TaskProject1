# from django.shortcuts import render
from rest_framework import viewsets

from .serializers import EmployeeSerializer, DepSerializer, TransferSerializer, AppointmentSerializer
from .models import Employee, Dep, Transfer, Appointment


# Create your views here.


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('id')
    serializer_class = EmployeeSerializer


class DepViewSet(viewsets.ModelViewSet):
    queryset = Dep.objects.all().order_by('code')
    serializer_class = DepSerializer


class TransferViewSet(viewsets.ModelViewSet):
    queryset = Transfer.objects.all().order_by('date_transfer')
    serializer_class = TransferSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all().order_by('date_appointment')
    serializer_class = AppointmentSerializer