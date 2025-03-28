import random
from datetime import timedelta, date
from django.core.management.base import BaseCommand
from tasks.models import Tarefa

class Command(BaseCommand):
    help = "popula o banco de dados com 15 tarefas aleatórias"

    def handle(self, *args, **kwargs):
        Tarefa.objects.all().delete()
        
        situacoes = ["nova", "em_andamento", "concluida", "atrasada"]
        hoje = date.today()
        tarefas = []

        for i in range(1, 16):
            titulo = f"Tarefa {i}"
            descricao = f"Descrição da tarefa {i}"
            prazo = hoje + timedelta(days=random.randint(-10, 20))  # a ideia é de poder usar uma data q esteja tanto no futuro/passado
            situacao = random.choice(situacoes)

            tarefas.append(Tarefa(titulo=titulo, descricao=descricao, prazo=prazo, situacao=situacao))

        Tarefa.objects.bulk_create(tarefas)

        self.stdout.write(self.style.SUCCESS("Banco de dados populado"))
