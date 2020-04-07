from django.contrib import admin

from .models import User, Equipment, Measurement, Bill

for model in [User, Equipment, Measurement, Bill]:
    admin.site.register(model)
