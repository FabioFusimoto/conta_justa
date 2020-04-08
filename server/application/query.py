from ..connectors.database import findAllEquipmentsForUser, findAllMeasurementsForYearMonth, findAllMeasurementsForYearMonthEquipment, findUserById
from ..constants import SHARED_USER_ID
from ..domain.domain import calculateBillAmount

def getBillParameters(year, month):
    totalConsumption = 0.0
    mList = findAllMeasurementsForYearMonth(year=year, month=month)
    for m in mList:
        totalConsumption += float(m.consumption)

    totalAmount = calculateBillAmount(consumption=totalConsumption)
    return totalConsumption, totalAmount

def getUserConsumption(user, year, month):
    equipmentsForUser = findAllEquipmentsForUser(user=user)
    consumption = 0.0
    for e in equipmentsForUser:
        for m in findAllMeasurementsForYearMonthEquipment(e, year, month):
            consumption += float(m.consumption)

    return consumption

def getSharedConsumption(year, month):
    sharedUser = findUserById(id=SHARED_USER_ID)
    return getUserConsumption(user=sharedUser, year=year, month=month)
