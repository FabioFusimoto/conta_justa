from django.db import IntegrityError
from ..models import User, Equipment, Measurement, Bill

# User
def findUserByName(name):
    return User.objects.all().filter(name=name)[:1]

def findUserById(id):
    return User.objects.all().filter(id=id)[:1]

def findAllUsers():
    return User.objects.all()

def createUser(name):
    try:
        newUser = User(name=name)
        newUser.save()
    except IntegrityError:
        return(False)

    return(True)

# Equipment
def createEquipment(name, user):
    try:
        newEquipment = Equipment(name=name, user=user)
        newEquipment.save()
        return newEquipment
    except IntegrityError:
        return False

def findEquipmentByName(name):
    return Equipment.objects.all().filter(name=name)[:1]

# Measurement
def createMeasurement(equipment, consumption):
    newMeasurement = Measurement(equipment=equipment, consumption=consumption) # o campo measuredAt é automaticamente setado para now(), ver o models.py
    newMeasurement.save()

# Bill
def createBill(user, year, month, consumption, amount):
    newBill(user=user, year=year, month=month, consumption=consumption, amount=amount)
    newBill.save()

def findBill(user, year, month):
    return Bill.objects.all().filter(user=user, year=year, month=month)
