from rest_framework import serializers

# from rest_framework.fields import SerializerMethodField

from .models import Employee, Dep, Transfer, Appointment


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'


class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    # transfer_current = TransferSerializer()
    transfer_current = serializers.ReadOnlyField()
    dep_current = serializers.ReadOnlyField()

    class Meta:
        model = Employee
        fields = "__all__"


class DepSerializer(serializers.ModelSerializer):
    appointment_current = serializers.ReadOnlyField()
    head_current = serializers.ReadOnlyField()

    class Meta:
        model = Dep
        fields = "__all__"
