from ..application.commands import addUser, addEquipment
from ..constants import ADD_USER_EVENT, ADD_EQUIPMENT_EVENT

def handler(eventName, **kwargs):
    if eventName == ADD_USER_EVENT:
        userName = kwargs['userName']
        addUser(name=userName)
    elif eventName == ADD_EQUIPMENT_EVENT:
        userName = kwargs['userName']
        equipmentName = kwargs['equipmentName']
        shared = kwargs['shared']
        addEquipment(userName=userName, equipmentName=equipmentName, shared=shared)
    else:
        print('Evento não reconhecido:' + str(eventName))
