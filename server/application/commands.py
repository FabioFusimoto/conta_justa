# SELECT
from ..connectors.database import findUserById, findUserByName, findAllUsers, findEquipmentByName, findBill

# INSERT
from ..connectors.database import createUser, createEquipment, createMeasurement

from ..constants import SHARED_USER_ID

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
        createMeasurement(equipment=relatedEquipment, consumption=consumption)
        return "Medição adicionada com sucesso"
    else:
        return "O equipamento com o nome fornecido não existe"
