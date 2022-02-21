from django.db import models

class Teams(models.Model):
    name_team = models.CharField('full name', max_length=20)
    coach = models.ForeignKey('Coach', on_delete=models.DO_NOTHING)

class Athletes(models.Model):

    full_name = models.CharField('Full name', max_length=50)
    email = models.EmailField('Email', max_length=100)
    birth_date = models.DateField('Birth date')
    federado = models.BooleanField('Federedo', default=False)
    team = models.ForeignKey("Teams", on_delete=models.DO_NOTHING)
    cpf = models.CharField('CPF', max_length=11 )
    rg = models.CharField('RG', max_length=11 )

class Coach(models.Model):

    full_name = models.CharField('Full name',max_length=50)
    email = models.EmailField('Email',max_length=100)
    birth_date = models.DateField('Birth date')
    team = models.ForeignKey("Teams", on_delete=models.DO_NOTHING)
    cpf = models.CharField('CPF', max_length=11 )
    rg = models.CharField('RG', max_length=9 )

    