from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)

class Equipment(models.Model):
    name = models.CharField(max_length=200)

class UserEquipment(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    equipmentId = models.ForeignKey(Equipment, on_delete=models.CASCADE)

class Measurement(models.Model):
    equipmentId = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    measuredAt = models.DateTimeField(auto_now_add=True)
