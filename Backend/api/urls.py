from django.urls import path
from numpy import add
from . import views


urlpatterns = [
    path('',views.getData),
    path('add/',views.addItem),
]