import datetime
from django.db import IntegrityError
from django.db.models import Q
from ..models import User, Equipment, Measurement, Bill, UserBill
from ..constants import SHARED_USER_ID

# User
def findAllUsers():
    return User.objects.all().filter(~Q(id = SHARED_USER_ID)) # the ~Q excludes the shared user

def findUserByName(name):
    return User.objects.all().filter(name=name)[:1]

def findUserById(id):
    return User.objects.all().filter(id=id)[:1]

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
    newMeasurement = Measurement(equipment=equipment, consumption=consumption) # o campo measured_at é automaticamente setado para now(), ver o models.py
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
    return Measurement.objects.all().filter(measured_at__range=(start, finish))

def findAllMeasurementsForYearMonthEquipment(equipment, year, month):
    start = datetime.datetime(year=year, month=month, day=1)
    newMonth = month + 1
    newYear = year
    if month == 13:
        nextMonth = 1
        newYear = newYear + 1
    finish = datetime.datetime(year=newYear, month=newMonth, day=1)

    return Measurement.objects.all().filter(equipment=equipment, measured_at__range=(start, finish))

# Bill
def findBill(year, month):
    return Bill.objects.all().filter(year=year, month=month)[:1]

def createBill(year, month, consumption, amount):
    newBill = Bill(year=year, month=month, consumption=consumption, amount=amount)
    newBill.save()
    return newBill

def updateBill(year, month, consumption, amount):
    billToUpdate = Bill.objects.get(year=year, month=month)
    billToUpdate.consumption = consumption
    billToUpdate.amount = amount
    billToUpdate.updated_at = datetime.datetime.now()
    billToUpdate.save()
    return billToUpdate

# UserBill
def findUserBill(bill, user):
    return UserBill.objects.all().filter(bill=bill, user=user)[:1]

def updateUserBill(bill, user, consumption, amount):
    userBillToUpdate = UserBill.objects.get(bill=bill, user=user)
    userBillToUpdate.consumption = consumption
    userBillToUpdate.amount = amount
    userBillToUpdate.updated_at = datetime.datetime.now()
    userBillToUpdate.save()
    return userBillToUpdate

def createUserBill(bill, user, consumption, amount):
    newUserBill = UserBill(bill=bill, user=user, consumption=consumption, amount=amount)
    newUserBill.save()
    return newUserBill
