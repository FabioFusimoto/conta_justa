from django.http import HttpResponse
import django_rq
import time
import json

from .application.commands import addUser, addEquipment
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
    if request.method == 'POST' and equipmentName and userName:
        return HttpResponse(
            addEquipment(equipmentName=equipmentName, userName=userName, shared=shared))
    else:
        return HttpResponse("Invalid request")

def updateMeasurement(request):
    body = json.loads(request.body)
    equipmentID = body["equipmentID"]
    consumption = body["consumption"]
    measuredAt = body["measuredAt"]
    if request.method == "POST":
        return HttpResponse(
            updateMeasure(equipmentID=equipmentID, consumption=consumption, measureAt=measuredAt)
        )
    else:
        return HttpResponse("Invalid request")

def newUserViaHandler(request):
    userName = json.loads(request.body)['name']
    if request.method == 'POST':
        django_rq.enqueue(handler, eventName=ADD_USER_EVENT, userName=userName)
        return HttpResponse("Evento de criação de novo usuário adicionado à fila")
    else:
        return HttpResponse("Invalid request")

def newEquipmentViaHandler(request):
    body = json.loads(request.body)
    equipmentName = body['equipmentName']
    userName = body['userName']
    shared = body['shared']
    if request.method == 'POST' and equipmentName and userName:
        django_rq.enqueue(handler, eventName=ADD_EQUIPMENT_EVENT, equipmentName=equipmentName, userName=userName, shared=shared)
        return HttpResponse("Evento de criação de novo equipamento adicionado à fila")
    else:
        return HttpResponse("Invalid request")

def updateMeasurementViaHandler(request):
    body = json.loads(request.body)
    equipmentID = body["equipmentID"]
    consumption = body["consumption"]
    measuredAt = body["measuredAt"]
    if request.method == "POST":
        django_rq.enqueue(handler, eventName=UPDATE_MEASURE_EVENT, equipmentID=equipmentID, consumption=consumption, measureAt=measuredAt)
        return HttpResponse("Evento de atualização de medida adicionado à fila")
    else:
        return HttpResponse("Invalid request")
