# SELECT
from ..connectors.database import findUserById, findUserByName, findAllUsers, findEquipmentByName, findBill, findUserBill

# INSERT
from ..connectors.database import createUser, createEquipment, createMeasurement, createBill, createUserBill

# UPDATE
from ..connectors.database import updateBill, updateUserBill

from ..constants import SHARED_USER_ID
from .query import getBillParameters, getUserConsumption, getSharedConsumption
from ..domain.domain import calculateUserBillAmount, calculateUserConsumption

# User
def addUser(id, name):
    if name:
        if createUser(id=id, name=name):
            return "Usuário criado com sucesso"
        else:
            return "Erro: O nome do usuário deve ser único"
    else:
        return "Erro: O nome não foi fornecido"

# Equipment
def addEquipment(equipmentName, userName='', shared=False):
    if shared:
        relatedUser = findUserById(id=SHARED_USER_ID)[0]
    else:
        relatedUser = findUserByName(name=userName)[0]

    if relatedUser.id:
        newEquipment = createEquipment(name=equipmentName, user=relatedUser)
        if newEquipment:
            if shared:
                return "Equipamento compartilhado '" + equipmentName + "' criado"
            else:
                return "Equipamento '" + equipmentName + "' do usuário " + userName + " criado"
        else:
            return "O equipamento com o nome fornecido já está registrado. Escolha outro nome"
    else:
        return "O nome de usuário fornecido não existe"

# Measurement
def addMeasurement(equipmentName, consumption, measuredAt):
    relatedEquipment = findEquipmentByName(name=equipmentName)[0]

    if relatedEquipment.id:
        newMeasurement = createMeasurement(equipment=relatedEquipment, consumption=consumption, measuredAt=measuredAt)
        user = relatedEquipment.user
        year = newMeasurement.measured_at.year
        month = newMeasurement.measured_at.month
        createOrUpdateBill(year, month)
        return "Medição adicionada com sucesso"
    else:
        return "O equipamento com o nome fornecido não existe"

# Bill
def createOrUpdateBill(year, month):
    consumption, amount = getBillParameters(year=year, month=month)
    if len(findBill(year=year, month=month)) > 0:
        bill = updateBill(year, month, consumption, amount)
    else:
        bill = createBill(year, month, consumption, amount)
    createOrUpdateUserBills(bill=bill)

# User Bill
def createOrUpdateUserBills(bill):
    sharedConsumption = getSharedConsumption(month=bill.month, year=bill.year)
    users = findAllUsers()
    for u in users:
        selfConsumption = getUserConsumption(user=u, month=bill.month, year=bill.year)
        userAmount = calculateUserBillAmount(sharedConsumption, selfConsumption, bill.consumption, bill.amount, len(users))
        userConsumption = calculateUserConsumption(sharedConsumption, selfConsumption, len(users))
        if len(findUserBill(bill=bill, user=u)) > 0:
            updateUserBill(bill=bill, user=u, consumption=userConsumption, amount=userAmount)
        else:
            createUserBill(bill=bill, user=u, consumption=userConsumption, amount=userAmount)
