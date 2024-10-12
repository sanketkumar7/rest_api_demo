from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Employee
from .serializers import employee_serializer
from rest_framework.renderers import JSONRenderer as json_r
# Create your views here.
@csrf_exempt
def employee_crud(request):
    if request.method=='GET':
        print('I am here...')
        json_data=request.body
        json_string=json_data.decode()
        python_dict=json.loads(json_string)
        id=python_dict.get('id',None)
        if id:
            emp=Employee.objects.get(id=id)
            serializer=employee_serializer(emp)
            json_data=json_r().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        qs=Employee.objects.all()
        serializer=employee_serializer(qs,many=True)
        json_data=json_r().render(serializer.data)
        return HttpResponse(json_data,content_type='applicatiom/json')
    
    elif request.method=='POST':
        json_data=request.body
        json_string=json_data.decode()
        python_dict=json.loads(json_string)
        serializer=employee_serializer(data=python_dict)
        if serializer.is_valid():
            serializer.save()
            msg={'msg':'data saved successfully.'}
            json_data=json_r().render(msg)
            return HttpResponse(json_data,content_type='application/json')
        json_data=json_r().render(msg)
        return HttpResponse(json_data,content_type='application/json')
    elif request.method=='PUT':
        json_data=request.body
        json_string=json_data.decode()
        python_dict=json.loads(json_string)
        emp=Employee.objects.get(id=python_dict.get('id'))
        serializer=employee_serializer(emp,data=python_dict,partial=True)
        if serializer.is_valid():
            serializer.save()
            msg={'msg':'Data has been updated successfully.'}
            json_data=json_r().render(msg)
            return HttpResponse(json_data,content_type='application/json')
        json_data=json_r().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')

