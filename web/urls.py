from django.contrib import admin
from django.urls import path
from .views import Test

urlpatterns = [
    path('', Test.test()),
]
