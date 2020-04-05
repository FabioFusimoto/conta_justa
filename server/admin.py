from django.contrib import admin

from .models import User, Equipment, UserEquipment, Measurement

for model in [User, Equipment, UserEquipment, Measurement]:
    admin.site.register(model)
