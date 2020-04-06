from ..application.commands import addUser, addEquipment, updateMeasure
from ..constants import ADD_USER_EVENT, ADD_EQUIPMENT_EVENT, UPDATE_MEASURE_EVENT

def handler(eventName, **kwargs):
    if eventName == ADD_USER_EVENT:
        userName = kwargs['userName']
        addUser(name=userName)
    elif eventName == ADD_EQUIPMENT_EVENT:
        userName = kwargs['userName']
        equipmentName = kwargs['equipmentName']
        shared = kwargs['shared']
        addEquipment(userName=userName, equipmentName=equipmentName, shared=shared)
    elif eventName == UPDATE_MEASURE_EVENT:
        equipmentID = kwargs['equipmentID']
        consumption = kwargs['consumption']
        measuredAt = kwargs['measuredAt']
        updateMeasure(equipmentID=equipmentID, consumption=consumption, measuredAt=measuredAt)
    else:
        print('Evento não reconhecido:' + str(eventName))
