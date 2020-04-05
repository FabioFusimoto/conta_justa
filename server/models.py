from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return(
            "ID:" + str(self.id) + "\n"
            "Nome:" + self.name
        )

class Equipment(models.Model):
    name = models.CharField(max_length=200, unique=True)
    shared = models.BooleanField(default=False)

    def __str__(self):
        return(
            "ID:" + str(self.id) + "\n"
            "Nome:" + self.name + "\n"
            "Compartilhado?: " + str(self.shared)
        )

class UserEquipment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)

class Measurement(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    consumption = models.DecimalField(default=0.0, max_digits=10, decimal_places=3)
    measuredAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return(
            "ID:" + str(self.id) + "\n"
            "Medição:" + str(self.consumption) + "Wh \n"
            "Medido em: " + str(self.measuredAt)
        )
