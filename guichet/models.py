from django.db import models


class Login(models.Model):
    cne = models.CharField(max_length=20)
    cin = models.CharField(max_length=20)
# Create your models here.
