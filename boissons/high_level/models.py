from django.db import models


class MatierePremiere(models.Model):
    nom = models.CharField(max_length=100)
    stock = models.FloatField()
    emprise = models.FloatField()

    def __str__(self):
        return self.nom


class QuantiteMatierePremiere(models.Model):
    quantite = models.IntegerField()
    matiere_premiere = models.ForeignKey(
        MatierePremiere,
        on_delete=models.PROTECT,
    )

    class Meta:
        abstract = True


class Localisation(models.Model):
    nom = models.CharField(max_length=100)
    taxes = models.FloatField()
    prix_m2 = models.FloatField()

    def __str__(self):
        return self.nom


class Local(models.Model):
    nom = models.CharField(max_length=100)
    surface = models.FloatField()
    localisation = models.ForeignKey(Localisation, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom


class Energie(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.FloatField()
    localisation = models.ForeignKey(Localisation, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom


class DebitEnergie(models.Model):
    debit = models.FloatField()
    energie = models.ForeignKey(Energie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.debit} de {self.energie}"
