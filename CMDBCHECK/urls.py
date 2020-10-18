from django.contrib import admin
from django.urls import path, include

from CMDBCHECK import views

urlpatterns = [
    path('CMDBCHECK/',views.scanhots,name='scanhots'),
]