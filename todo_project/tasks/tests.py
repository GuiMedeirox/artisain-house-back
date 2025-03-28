from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Tarefa  


class TarefaAPITestCase(APITestCase):
    
    def setUp(self):
        """
        criando algumas tarefas p servirem de teste
        """
        self.tarefa1 = Tarefa.objects.create(
            titulo="Tarefa Teste 1",
            descricao="Descrição da Tarefa 1",
            prazo="2024-04-01",
            situacao="nova"
        )

        self.tarefa2 = Tarefa.objects.create(
            titulo="Tarefa Teste 2",
            descricao="Descrição da Taref-a 2",
            prazo="2024-04-10",
            situacao="em_andamento"
        )

        self.tarefa_list_url = reverse("tarefa-list")  

    def test_listar_tarefas(self):
        """
        teste pra ver se o endpoint de tarefas esta funcionando certinho e retornando os 2 itens que foram inseridos
        """
        response = self.client.get(self.tarefa_list_url)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  
    
    def test_criar_tarefa(self):
        """
        tentar criar de uma nova tarefa.
        """
        data = {
            "titulo": "Nova Tarefa",
            "descricao": "Descrição da nova tarefa",
            "prazo": "2024-05-01",
            "situacao": "nova"
        }
        response = self.client.post(self.tarefa_list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tarefa.objects.count(), 3)  

    def test_visualizar_tarefa(self):
        """
        tenta obter uma única tarefa.
        """
        url = reverse("tarefa-detail", args=[self.tarefa1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["titulo"], self.tarefa1.titulo)

    def test_atualizar_tarefa(self):
        """
        tenta atualizar uma tarefa existente.
        """
        url = reverse("tarefa-detail", args=[self.tarefa1.id])
        data = {"situacao": "concluida"}
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.tarefa1.refresh_from_db()  
        self.assertEqual(self.tarefa1.situacao, "concluida")

    def test_excluir_tarefa(self):
        """
        teste p deletar uma tarefa.
        """
        url = reverse("tarefa-detail", args=[self.tarefa1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Tarefa.objects.count(), 1)  

    def test_criar_tarefa_falha(self):
        """
        teste p criar uma tarefa e retornar erro e retornar que o field faltando é o titulo
        """
        data = {
            "descricao": "Tarefa sem título",
            "prazo": "2024-06-01",
            "status": "nova"
        }
        response = self.client.post(self.tarefa_list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("titulo", response.data)  
