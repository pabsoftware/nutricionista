from django.db import models
from usuarios.models import CustomUser

# Create your models here.

class Pacientes(models.Model):
    choices_sexo = (('F', 'Feminino'),
                   ('M', 'Masculino'))
    nome = models.CharField(max_length=80)
    sexo = models.CharField(max_length=1, choices=choices_sexo)
    idade = models.IntegerField()
    email = models.EmailField()
    telefone = models.CharField(max_length=19)
    nutri = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


    class Meta: 
        verbose_name_plural = ("pacientes")
        db_table = 'pacientes'
    
    def __str__(self):
         return self.nome

   