from ..application.commands import addUser, addEquipment, addMeasurement
from ..constants import ADD_USER_EVENT, ADD_EQUIPMENT_EVENT, ADD_MEASURE_EVENT


def handler(eventName, **kwargs):
    if eventName == ADD_USER_EVENT:
        userName = kwargs['userName']
        addUser(name=userName)
    elif eventName == ADD_EQUIPMENT_EVENT:
        userName = kwargs['userName']
        equipmentName = kwargs['equipmentName']
        shared = kwargs['shared']
        addEquipment(userName=userName, equipmentName=equipmentName, shared=shared)
    elif eventName == ADD_MEASURE_EVENT:
        equipmentName = kwargs["equipmentName"]
        consumption = kwargs["consumption"]
        addMeasurement(equipmentName=equipmentName, consumption=consumption)
    else:
        print('Evento não reconhecido:' + str(eventName))
