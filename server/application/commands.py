# SELECT
from ..connectors.database import findUserById, findUserByName, findAllUsers, findEquipmentByName, findBill

# INSERT
from ..connectors.database import createUser, createEquipment, createMeasurement, createBill

# UPDATE
from ..connectors.database import updateBill

from ..constants import SHARED_USER_ID
from .query import getBillParameters

# User
def addUser(name):
    if name:
        if createUser(name=name):
            return "Usuário criado com sucesso"
        else:
            return "Erro: O nome do usuário deve ser único"
    else:
        return "Erro: O nome não foi fornecido"

# Equipment
def addEquipment(equipmentName, userName, shared=False):
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
def addMeasurement(equipmentName, consumption):
    relatedEquipment = findEquipmentByName(name=equipmentName)[0]

    if relatedEquipment.id:
        newMeasurement = createMeasurement(equipment=relatedEquipment, consumption=consumption)
        user = relatedEquipment.user
        year = newMeasurement.measuredAt.year
        month = newMeasurement.measuredAt.month
        createOrUpdateBill(year, month)
        return "Medição adicionada com sucesso"
    else:
        return "O equipamento com o nome fornecido não existe"

# Bill
def createOrUpdateBill(year, month):
    sharedUser = findUserById(id=SHARED_USER_ID)[0]
    consumption, amount = getBillParameters(year=year, month=month)
    if len(findBill(year=year, month=month)) > 0:
        updateBill(year, month, consumption, amount)
    else:
        createBill(year, month, consumption, amount)
