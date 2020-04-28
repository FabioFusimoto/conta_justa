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
    measured_at = models.DateTimeField()

    def __str__(self):
        return(
            "ID: " + str(self.id) + "\n"
            "Medição: " + str(self.consumption) + "Wh \n"
            "Medido em: " + str(self.measured_at)
        )

class Bill(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    consumption = models.DecimalField(max_digits=20, decimal_places=3)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return(
            "ID: " + str(self.id) + "\n"
            "Mês: " + str(self.month) + "/" + str(self.year) + "\n"
            "Consumo: " + str(self.consumption) + "\n"
            "Valor: " + str(self.amount) + "\n"
            "Atualizada em: " + str(self.updated_at)
        )

class UserBill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    consumption = models.DecimalField(max_digits=20, decimal_places=3)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return(
            "ID: " + str(self.id) + "\n"
            "Mês: " + str(self.bill.month) + "/" + str(self.bill.year) + "\n"
            "Consumo: " + str(self.consumption) + "\n"
            "Valor: " + str(self.amount) + "\n"
            "Atualizada em: " + str(self.updated_at)
        )
