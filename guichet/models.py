from django.db import models



class Etudiant(models.Model):
    #user: models.OneToOneField()
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    cin = models.CharField(max_length=255, unique=True)
    cne = models.CharField(max_length=255, unique=True)
    num_tel = models.CharField(max_length=255)
    email = models.EmailField()
    date_de_naissance = models.DateField(null=True)
    date_d_inscription = models.DateField(null=True)

    def __str__(self):
        return f"{self.nom} {self.prenom}"
