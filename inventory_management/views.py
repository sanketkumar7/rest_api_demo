from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import inventory_serializer,inventory_serializer2
from .models import Inventory
from django.forms.models import model_to_dict

class json_data_using_api_view(APIView):
    def get(self,request,id):
        if id:
            try:
                item=Inventory.objects.get(item_id=id)
                serializer=inventory_serializer(item)
                return Response({'item':serializer.data})
            except Inventory.DoesNotExist:
                return Response({'msg':f'item with id {id} does not found.'},status=400)
            except Inventory.MultipleObjectsReturned:
                return Response({'msg':'Multiple objects found.'})
            
    def post(self,request):
        data=request.data
        serializer=inventory_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':f"Item is added successfully.{serializer.data}"})
        return Response(serializer.errors,status=400)
    
    def put(self,request,id):
        try:
            item=Inventory.objects.get(item_id=id)
        except Inventory.DoesNotExist:
            return Response({'msg':"Item not found"},status=400)
        except Inventory.MultipleObjectsReturned:
            return Response({'msg':'Multiple item with same id'},status=400)
        else:
            data=request.data
            serializer=inventory_serializer2(instance=item,data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Item updated successfully.'})
            return Response(serializer.errors)
        
    def delete(self,request,id):
        try:
            item=Inventory.objects.get(item_id=id)
        except Inventory.DoesNotExist:
            return Response({'msg':'Item not found'},status=400)
        except Inventory.MultipleObjectsReturned:
            return Response({'msg':'multiple Item found'})
        else:
            item.delete()
            return Response({'msg':'Item deleted successfully.'})
        
        
