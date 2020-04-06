from django.db import IntegrityError
from ..models import User, Equipment, UserEquipment, Measurement

# User
def findUserByName(name):
    return User.objects.all().filter(name=name)[:1]

def findAllUsers():
    return User.objects.all()

def findEquipmentByID(equipmentID):
    return Equipment.objects.all().filter(id = equipmentID)

def findMeasurementByEquipment(equipment):
    return Measurement.objects.all().filter(equipment=equipment)

def createUser(name):
    try:
        newUser = User(name=name)
        newUser.save()
    except IntegrityError:
        return(False)

    return(True)

# Equipment
def createEquipment(name, shared):
    try:
        newEquipment = Equipment(name=name, shared=shared)
        newEquipment.save()
        return newEquipment
    except IntegrityError:
        return False

# UserEquipment
def createUserEquipment(user, equipment):
    newUserEquipment = UserEquipment(user=user, equipment=equipment)
    newUserEquipment.save()

# Measurement
def createMeasurement(equipmentId, consumption, measuredAt):
    newMeasurement(equipmentId=equipmentId, consumption=consumption, measuredAt=measuredAt)
    newMeasurement.save()

def updateMeasurement(equipment, consumption, measuredAt):
    measurement = findMeasurementByEquipment(equipment)
    measurement.consumption += consumption
    measurement.measuredAt = measuredAt
    measurement.save()
