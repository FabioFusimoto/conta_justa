import datetime
from django.db import IntegrityError
from ..models import User, Equipment, Measurement, Bill
from ..constants import SHARED_USER_ID

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

def findAllEquipmentsForUser(user):
    return Equipment.objects.all().filter(user=user)

# Measurement
def createMeasurement(equipment, consumption):
    newMeasurement = Measurement(equipment=equipment, consumption=consumption) # o campo measuredAt é automaticamente setado para now(), ver o models.py
    newMeasurement.save()
    return newMeasurement

def findAllMeasurementsForYearMonth(year, month):
    start = datetime.datetime(year=year, month=month, day=1)
    newMonth = month + 1
    newYear = year
    if month == 13:
        nextMonth = 1
        newYear = newYear + 1
    finish = datetime.datetime(year=newYear, month=newMonth, day=1)
    return Measurement.objects.all().filter(measuredAt__range=(start, finish))

def findAllMeasurementsForYearMonthEquipment(equipment, year, month):
    start = datetime.datetime(year=year, month=month, day=1)
    newMonth = month + 1
    newYear = year
    if month == 13:
        nextMonth = 1
        newYear = newYear + 1
    finish = datetime.datetime(year=newYear, month=newMonth, day=1)

    return Measurement.objects.all().filter(equipment=equipment, measuredAt__range=(start, finish))

# Bill
def findBill(year, month):
    return Bill.objects.all().filter(year=year, month=month)[:1]

def createBill(year, month, consumption, amount):
    newBill = Bill(year=year, month=month, consumption=consumption, amount=amount)
    newBill.save()

def updateBill(year, month, consumption, amount):
    billToUpdate = Bill.objects.get(year=year, month=month)
    billToUpdate.consumption = consumption
    billToUpdate.amount = amount
    billToUpdate.save()
