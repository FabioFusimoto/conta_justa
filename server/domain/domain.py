from ..constants import CONSUMPTION_FEE

def calculateBillAmount(consumption):
    return consumption * CONSUMPTION_FEE

def calculateUserConsumption(sharedConsumption, selfConsumption, userCount):
    return selfConsumption + (sharedConsumption/userCount)

def calculateUserBillAmount(sharedConsumption, selfConsumption, totalConsumption, billAmount, userCount):
    sharedPart = (sharedConsumption/totalConsumption) * (billAmount/userCount)
    if totalConsumption > sharedConsumption:
        individualPart = (billAmount - (sharedPart * userCount)) * selfConsumption / (totalConsumption - sharedConsumption)
    else:
        individualPart = 0.0

    return (sharedPart + individualPart)
