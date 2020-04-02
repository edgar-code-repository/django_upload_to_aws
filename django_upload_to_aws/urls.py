from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('upload_aws.urls'))
]
