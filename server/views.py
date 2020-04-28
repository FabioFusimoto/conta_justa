from django.http import HttpResponse
import django_rq
import datetime
import json

from .application.commands import addUser, addEquipment, addMeasurement
from .connectors.queue import handler
from .constants import ADD_USER_EVENT, ADD_EQUIPMENT_EVENT

from .scripts.populate_database import populateDatabase

def printMessage(header, message):
    print(header)
    print(message)

def index(request):
    django_rq.enqueue(printMessage, "This is the header", message="Test message")
    return HttpResponse("Hello, you are at the server index")

def newUser(request):
    body = json.loads(request.body)
    if 'id' in body.keys():
        id = body['id']
    else:
        id = False
    name = body['name']
    if request.method == 'POST':
        return HttpResponse(addUser(id=id, name=name))
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
    measuredAt = datetime.datetime.strptime(body['measuredAt'], '%d/%m/%Y %H:%M:%S')
    if request.method == 'POST' and equipmentName and consumption:
        return HttpResponse(
            addMeasurement(equipmentName=equipmentName, consumption=consumption, measuredAt=measuredAt)
        )
    else:
        return HttpResponse("Invalid request")

def fillDatabase(request):
    measurementsAdded = populateDatabase()
    return HttpResponse(str(measurementsAdded) + ' new measurements added')
