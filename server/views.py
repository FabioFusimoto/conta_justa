from django.http import HttpResponse
import django_rq
import time
import json

from .application.commands import addUser, addEquipment, addMeasurement
from .connectors.queue import handler
from .constants import ADD_USER_EVENT, ADD_EQUIPMENT_EVENT

def printMessage(header, message):
    print(header)
    print(message)

def index(request):
    django_rq.enqueue(printMessage, "This is the header", message="Test message")
    return HttpResponse("Hello, you are at the server index")

def newUser(request):
    name = json.loads(request.body)['name']
    if request.method == 'POST':
        return HttpResponse(addUser(name=name))
    else:
        return HttpResponse("Invalid request")

def newEquipment(request):
    body = json.loads(request.body)
    equipmentName = body['equipmentName']
    userName = body['userName']
    shared = body['shared']
    if request.method == 'POST' and equipmentName and (userName or shared):
        return HttpResponse(
            addEquipment(equipmentName=equipmentName, userName=userName, shared=shared))
    else:
        return HttpResponse("Invalid request")

def newMeasurement(request):
    body = json.loads(request.body)
    equipmentName = body['equipmentName']
    consumption = body['consumption']
    if request.method == 'POST' and equipmentName and consumption:
        return HttpResponse(
            addMeasurement(equipmentName=equipmentName, consumption=consumption)
        )
    else:
        return HttpResponse("Invalid request")
