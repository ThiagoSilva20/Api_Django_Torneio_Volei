from django.db import models

class Coach(models.Model):
    full_name = models.CharField('Full name',max_length=50)
    email = models.EmailField('Email',max_length=100)
    cpf = models.CharField('CPF', max_length=11 )
    rg = models.CharField('RG', max_length=9 )

class Teams(models.Model):
    name_team = models.CharField('full name', max_length=20)
    coaches = models.ForeignKey('Coach', on_delete=models.DO_NOTHING, default=0,)


class Athletes(models.Model):
    full_name = models.CharField('Full name', max_length=50)
    email = models.EmailField('Email', max_length=100)
    federado = models.BooleanField('Federedo', default=False)
    team = models.ForeignKey("Teams", on_delete=models.DO_NOTHING)
    cpf = models.CharField('CPF', max_length=11 )
    rg = models.CharField('RG', max_length=11 )


    