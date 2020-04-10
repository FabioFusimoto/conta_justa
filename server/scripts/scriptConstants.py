# ------------- Users ----------------
SHARED_USERNAME = 'Usuário compartilhado'
FABIO_USERNAME = 'Fábio Fusimoto Pires'
GABRIEL_USERNAME = 'Gabriel Roberti Passini'
GUSTAVO_USERNAME = 'Gustavo Ziyu Wang'

sharedUser = {
    'id': 1,
    'name': SHARED_USERNAME,
}

userFabio = {
    'id': 2,
    'name': FABIO_USERNAME,
}

userGabriel = {
    'id': 3,
    'name': GABRIEL_USERNAME,
}

userGustavo = {
    'id': 4,
    'name': GUSTAVO_USERNAME,
}

users = [sharedUser, userFabio, userGustavo, userGabriel]

# ------------ Equipments -------------
FABIO_NOTEBOOK = 'Notebook de Fábio'
FABIO_TELEVISION = 'Televisão de Fábio'
FABIO_PLAYSTATION = 'Playstation 4 de Fábio'
FABIO_LIGHT_FIXTURE = 'Luminária de Fábio'

equipmentNotebookFabio = {
    'name': FABIO_NOTEBOOK,
    'owner': FABIO_USERNAME,
    'consumption': 30,
    'probability': 0.1,
}

equipmentTelevisionFabio = {
    'name': FABIO_TELEVISION,
    'owner': FABIO_USERNAME,
    'consumption': 160,
    'probability': 0.05,
}

equipmentPlaystationFabio = {
    'name': FABIO_PLAYSTATION,
    'owner': FABIO_USERNAME,
    'consumption': 181,
    'probability': 0.05,
}

equipmentLightFixtureFabio = {
    'name': FABIO_LIGHT_FIXTURE,
    'owner': FABIO_USERNAME,
    'consumption': 4.5,
    'probability': 0.2,
}

GABRIEL_LAMP = 'Lâmpada de Gabriel'
GABRIEL_MINIBAR = 'Frigobar de Gabriel'
GABRIEL_XBOX = 'Xbox One de Gabriel'
GABRIEL_PHONE_CHARGER = 'Carregador de celular de Gabriel'

equipmentLampGabriel = {
    'name': GABRIEL_LAMP,
    'owner': GABRIEL_USERNAME,
    'consumption': 23,
    'probability': 0.4,
}

equipmentMinibarGabriel = {
    'name': GABRIEL_MINIBAR,
    'owner': GABRIEL_USERNAME,
    'consumption': 70,
    'probability': 0.98,
}

equipmentXboxGabriel = {
    'name': GABRIEL_XBOX,
    'owner': GABRIEL_USERNAME,
    'consumption': 289,
    'probability': 0.05,
}

equipmentPhoneChargerGabriel = {
    'name': GABRIEL_PHONE_CHARGER,
    'owner': GABRIEL_USERNAME,
    'consumption': 15,
    'probability': 0.05,
}

GUSTAVO_DESKTOP = 'Computador de Gustavo'
GUSTAVO_SWITCH = 'Nintendo Switch de Gustavo'
GUSTAVO_IPAD = 'iPad de Gustavo'
GUSTAVO_FAN = 'Ventilador de Gustavo'

equipmentDesktopGustavo = {
    'name': GUSTAVO_DESKTOP,
    'owner': GUSTAVO_USERNAME,
    'consumption': 240,
    'probability': 0.3,
}

equipmentSwitchGustavo = {
    'name': GUSTAVO_SWITCH,
    'owner': GUSTAVO_USERNAME,
    'consumption': 18,
    'probability': 0.1,
}

equipmentIPadGustavo = {
    'name': GUSTAVO_IPAD,
    'owner': GUSTAVO_USERNAME,
    'consumption': 12,
    'probability': 0.1,
}

equipmentFanGustavo = {
    'name': GUSTAVO_FAN,
    'owner': GUSTAVO_USERNAME,
    'consumption': 126,
    'probability': 0.02,
}

individualEquipments = [
    equipmentNotebookFabio,
    equipmentTelevisionFabio,
    equipmentPlaystationFabio,
    equipmentLightFixtureFabio,
    equipmentLampGabriel,
    equipmentMinibarGabriel,
    equipmentXboxGabriel,
    equipmentPhoneChargerGabriel,
    equipmentDesktopGustavo,
    equipmentSwitchGustavo,
    equipmentIPadGustavo,
    equipmentFanGustavo
]

SHARED_REFRIGERATOR = 'Geladeira compartilhada'
SHARED_AIR_CONDITIONER = 'Ar condicionado compartilhado'
SHARED_LAMPS = 'Lâmpadas compartilhadas'
SHARED_MODEM = 'Modem de internet compartilhado'

equipmentSharedRefrigerator = {
    'name': SHARED_REFRIGERATOR,
    'consumption': 250,
    'probability': 0.99,
}

equipmentSharedAirConditioner = {
    'name': SHARED_AIR_CONDITIONER,
    'consumption': 900,
    'probability': 0.2,
}

equipmentSharedLamps = {
    'name': SHARED_LAMPS,
    'consumption': 115,
    'probability': 0.3,
}

equipmentSharedModem = {
    'name': SHARED_MODEM,
    'consumption': 19,
    'probability': 0.99,
}

sharedEquipments = [
    equipmentSharedRefrigerator,
    equipmentSharedAirConditioner,
    equipmentSharedLamps,
    equipmentSharedModem,
]
