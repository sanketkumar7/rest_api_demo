from rest_framework import serializers
from .models import Employee

class employee_serializer(serializers.Serializer):
    eno=serializers.IntegerField()
    ename=serializers.CharField()
    esal=serializers.CharField()
    eaddr=serializers.CharField()
    def create(self,validated_data):
        return Employee.objects.create(**validated_data)
    def update(self,instance,validated_data):
        instance.eno=validated_data.get('eno',instance.eno)
        instance.ename=validated_data.get('ename',instance.ename)
        instance.eaddr=validated_data.get('eaddr',instance.eaddr)
        instance.esal=validated_data.get('esal',instance.esal)
        instance.save()
        return instance