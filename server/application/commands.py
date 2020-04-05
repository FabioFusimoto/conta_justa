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
