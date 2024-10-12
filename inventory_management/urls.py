from django.urls import path,include
from .views import *

urlpatterns=[
    path('api-auth',include('rest_framework.urls')),
    path('items/<int:id>',json_data_using_api_view.as_view()),
    path('items/',json_data_using_api_view.as_view())
]