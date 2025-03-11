from django.contrib import admin
from django.urls import path

from .views import intern_list, intern_detail

urlpatterns = [
    path("intern_list/", intern_list, name='intern_list'),
    path("intern_list/<int:id>", intern_detail, name="intern_detail"),

]