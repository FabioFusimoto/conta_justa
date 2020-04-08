# SELECT
from ..connectors.database import findUserByName, findAllUsers

# INSERT
from ..connectors.database import createUser, createEquipment, createUserEquipment, createMeasurement

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
    relatedUser=findUserByName(name=userName)[0]
    print(relatedUser)
    if relatedUser.id:
        newEquipment = createEquipment(name=equipmentName, shared=shared)
        relatedUserNames = []
        if newEquipment:
            if not shared:
                createUserEquipment(user=relatedUser, equipment=newEquipment)
                relatedUserNames.append(relatedUser.name)
            else:
                allUsers = findAllUsers()
                for user in allUsers:
                    createUserEquipment(user=user, equipment=newEquipment)
                    relatedUserNames.append(user.name)
            return ("Equipamento " + equipmentName + " adicionado com sucesso.\n" +
                    "Usuários relacionados ao equipamento: " + str(relatedUserNames))
        else:
            return "O equipamento com o nome fornecido já está registrado. Escolha outro nome"
    else:
        return "O nome de usuário fornecido não existe"
<<<<<<< Updated upstream
=======

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
>>>>>>> Stashed changes
