from django.db import models

class Tarefa(models.Model):
    STATUS_CHOICES = [
        ('nova', 'Nova'),
        ('em_andamento', 'Em Andamento'),
        ('concluida', 'Concluída'),
        ('cancelada', 'Cancelada'),
    ]
    
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=250, blank=True, null=True)
    prazo = models.DateField()
    data_conclusao = models.DateField(null=True, blank=True)
    situacao = models.CharField(max_length=20, choices=STATUS_CHOICES, default='nova')

    def __str__(self):
        return self.titulo
