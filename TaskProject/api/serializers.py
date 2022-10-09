from rest_framework import serializers

# from rest_framework.fields import SerializerMethodField

from .models import Employee, Dep, Transfer


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
    class Meta:
        model = Dep
        fields = "__all__"
