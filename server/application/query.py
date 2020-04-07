from ..connectors.database import findAllEquipmentsForUser, findAllMeasurementsForYearMonth
from ..constants import SHARED_USER_ID
from ..domain.domain import calculateBillAmount

def getBillParameters(year, month):
    sharedConsumption = 0.0
    mList = findAllMeasurementsForYearMonth(year=year, month=month)
    for m in mList:
        sharedConsumption += float(m.consumption)

    sharedAmount = calculateBillAmount(consumption=sharedConsumption)
    return sharedConsumption, sharedAmount
