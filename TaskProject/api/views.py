# from django.shortcuts import render
from rest_framework import viewsets

from .serializers import EmployeeSerializer, DepSerializer, EmployeeWithDepSerializer, DepWithEmployeeSerializer
from .models import Employee, Dep


# Create your views here.


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('id')
    serializer_class = EmployeeSerializer


class DepViewSet(viewsets.ModelViewSet):
    queryset = Dep.objects.all().order_by('id')
    serializer_class = DepSerializer


class EmployeeWithDepViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeWithDepSerializer


class DepWithEmployeeViewSet(viewsets.ModelViewSet):
    queryset = Dep.objects.all()
    serializer_class = DepWithEmployeeSerializer
