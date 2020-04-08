from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-user', views.newUser, name='add-user'),
    path('add-equipment', views.newEquipment, name='add-equipment'),
    path('add-measurement', views.newMeasurement, name='add-measurement'),
]
