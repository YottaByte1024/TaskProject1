from rest_framework import serializers
#from rest_framework.fields import SerializerMethodField

from .models import Employee, Dep


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class DepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dep
        fields = "__all__"


class EmployeeWithDepSerializer(serializers.ModelSerializer):

    dep_old_id = serializers.ReadOnlyField(source='id_dep_old.id')
    dep_new_id = serializers.ReadOnlyField(source='id_dep_new.id')
    dep_old_name = serializers.ReadOnlyField(source='id_dep_old.name')
    dep_new_name = serializers.ReadOnlyField(source='id_dep_new.name')
    dep_old_head_lastname = serializers.ReadOnlyField(source='id_dep_old.id_head.lastname')
    dep_new_head_lastname = serializers.ReadOnlyField(source='id_dep_new.id_head.lastname')
    dep_old_head_firstname = serializers.ReadOnlyField(source='id_dep_old.id_head.firstname')
    dep_new_head_firstname = serializers.ReadOnlyField(source='id_dep_new.id_head.firstname')


    class Meta:
        model = Employee
        fields = ['id', 'lastname', 'firstname',
                  'dep_old_id', 'dep_old_name', 'dep_old_head_lastname', 'dep_old_head_firstname',
                  'dep_new_id', 'dep_new_name', 'dep_new_head_lastname', 'dep_new_head_firstname',
                  'date_transfer']
