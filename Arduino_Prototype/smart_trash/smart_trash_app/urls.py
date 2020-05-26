from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('bin/<int:id>/', bin_by_id, name="bin_detail"),
    path('bin/update', update_bin, name="update_bin"),
]
