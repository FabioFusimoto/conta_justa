from .queue import handler

from server.models import Equipment

import random


def mock_measurement():
    listOfMeasures = []

    for equip in Equipment.objects.all():
        equipmentID = equip.id
        consumption = round(random.random(), 3)  # cria numero float aleatorio entre 0 e 1 com duas casas apos a virgula
        dictionary = {
            "equipmentID": equipmentID,
            "consumption": consumption,
        }
        listOfMeasures.append(dictionary)

    return listOfMeasures


def measurement_scheduler(eventName):
    listOfMeasures = mock_measurement()

    for dictionary in listOfMeasures:
        equipmentID = dictionary["equipmentID"]
        consumption = dictionary["consumption"]

        handler(eventName, equipmentID=equipmentID, consumption=consumption)
