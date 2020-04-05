from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-user', views.newUser, name='add-user'),
    path('add-equipment', views.newEquipment, name='add-equipment'),
    path('add-user-via-handler', views.newUserViaHandler, name='add-user-via-handler'),
    path('add-equipment-via-handler', views.newEquipmentViaHandler, name='add-equipment-via-handler'),
]
