from background_task import background

from .models import User, Equipment, UserEquipment, Measurement
from server.connectors.queue import handler

import random, datetime


@background(schedule=2)
def measurement_scheduler(eventName, **kwargs):
    list = kwargs["listOfMeasurement"]
    for dict in list:
        equipmentID = dict["equipmentID"]
        consumption = dict["consumption"]
        measuredAt = dict["measuredAt"]

        handler(eventName, equipmentID=equipmentID, consumption=consumption, measuredAt=measuredAt)

@background()
def mock_measures():
    listOfMeasures = []

    for equip in Equipment.objects.all():
        equipmentID = equip.id
        consumption = round(random.random(), 3) # cria numero float aleatorio entre 0 e 1 com duas casas apos a virgula
        measuredAt = datetime.datetime.now()
        dict = {
            "equipmentID": equipmentID,
            "consumption": consumption,
            "measuredAt": measuredAt,
        }
        listOfMeasures.append(dict)

    return listOfMeasures
