from django.urls import path,include
from .views import *

urlpatterns=[
    path('api-auth',include('rest_framework.urls')),
    path('drf-api',employee_crud,name='drf-api')
]