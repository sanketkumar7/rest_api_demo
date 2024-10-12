from rest_framework import serializers
from .models import Inventory
class inventory_serializer(serializers.ModelSerializer):
    class Meta:
        model=Inventory
        fields='__all__'
    def validate(self, attrs):
        validated_data=super().validate(attrs)
        item_id=validated_data.get('item_id')
        if Inventory.objects.filter(item_id=item_id).exists():
            raise serializers.ValidationError("Item already exists.")
        return validated_data
    
class inventory_serializer2(serializers.ModelSerializer):
    class Meta:
        model=Inventory
        fields='__all__'
    def validate(self, attrs):
        validated_data=super().validate(attrs)
        
        return validated_data