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
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return(
            "ID: " + str(self.id) + "\n"
            "Nome: " + self.name + "\n"
            "Pertence à: " + str(self.user.name)
        )

class Measurement(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    consumption = models.DecimalField(default=0.0, max_digits=10, decimal_places=3)
    measuredAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return(
            "ID: " + str(self.id) + "\n"
            "Medição: " + str(self.consumption) + "Wh \n"
            "Medido em: " + str(self.measuredAt)
        )

class Bill(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    consumption = models.DecimalField(max_digits=20, decimal_places=3)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    updatedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return(
            "ID: " + str(self.id) + "\n"
            "Mês: " + str(self.month) + "/" + str(year) + "\n"
            "Consumo: " + str(self.consumption) + "\n"
            "Valor: " + str(self.amount) + "\n"
            "Atualizada em: " + str(self.updatedAt)
        )
