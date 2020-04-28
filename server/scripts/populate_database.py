from datetime import datetime, timedelta
from random import random

from ..application.commands import addUser, addEquipment, addMeasurement
from ..constants import SHARED_USER_ID
from .scriptConstants import users, individualEquipments, sharedEquipments
from .helpers import getMeasurementCount

def populateDatabase():
    # Creating users
    for u in users:
        addUser(id=u['id'], name=u['name'])

    # Creating individual equipments
    for e in individualEquipments:
        addEquipment(equipmentName=e['name'], userName=e['owner'], shared=False)

    # Creating shared equipments
    for e in sharedEquipments:
        addEquipment(equipmentName=e['name'], shared=True)

    # Adding measurements
    # For every hour passed this year a measurement for each equipment will be created
    # So it's like a measurement is taken every {resolution} hours.
    # Consumption is measured in Wh. Probability is the likelihood of certain equipment being turned on
    # Every measurement will result in either 0 or consumption

    # The resolution modifier is an integer that dictates the measurement interval. Smaller values result in
    # more measurements (higher precision), but also means the script will take longer to run
    resolution = 10
    now = datetime.now()
    measurementDate = datetime(year=now.year, month=1, day=1)
    increment = timedelta(hours=resolution)

    # The consumption generation works as following: a number between 0 and 1 is generated,
    # if the generated value is lower than the equipment probability, it means the equipment
    # was off for that entire given hour. Higher probabilities will ultimately mean higher
    # overall consumption (factored by the own equipment consumption)

    dT = now - measurementDate
    hoursSinceStartOfTheYear = (dT.days) * 24 + (dT.seconds // 3600)
    measurementCount = hoursSinceStartOfTheYear * len(individualEquipments + sharedEquipments) // resolution
    print('\nHours since the start of the year: ' + str(hoursSinceStartOfTheYear))
    print('Measurement count: ' + str(measurementCount))

    measurementsAdded = 0

    if not (getMeasurementCount() > 0): # creates measurements only if database is empty
        while measurementDate < now:
            for e in (individualEquipments + sharedEquipments):
                threshold = random()
                if threshold < e['probability']:
                    addMeasurement(equipmentName = e['name'], consumption=(e['consumption'] * resolution), measuredAt=measurementDate)
                else:
                    addMeasurement(equipmentName = e['name'], consumption=0, measuredAt=measurementDate)
                if(measurementsAdded % 100) == 0:
                    print('\nProgress: ' + str(measurementsAdded) + '/' + str(measurementCount))
                measurementsAdded += 1
            measurementDate += increment
        print('\n>>>Added ' + str(measurementsAdded) + ' new measurements')

    return measurementsAdded
