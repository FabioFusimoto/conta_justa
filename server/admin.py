from django.contrib import admin

from .models import User, Equipment, Measurement, Bill, UserBill

for model in [User, Equipment, Measurement, Bill, UserBill]:
    admin.site.register(model)
