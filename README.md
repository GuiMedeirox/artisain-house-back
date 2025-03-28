# TO-DO List API

Este é um projeto de back-end desenvolvido com Django e Docker, com o objetivo de gerenciar tarefas (CRUD) usando um banco de dados PostgreSQL. O projeto também usa Docker Compose para facilitar o gerenciamento dos containers.

## Tecnologias

- **Django**: Framework de desenvolvimento web Python.
- **PostgreSQL**: Banco de dados relacional.
- **Docker**: Ferramenta para automatizar a implantação de aplicativos em containers.
- **Docker Compose**: Ferramenta para definir e executar aplicativos Docker multi-containers.

## Requisitos

- **Docker**: Você precisa do Docker e Docker Compose instalados na sua máquina. Caso ainda não tenha, siga as instruções de instalação [aqui](https://docs.docker.com/get-docker/).
- **Python 3.12**: Recomendado para o ambiente de desenvolvimento, mas o Docker cuidará dessa parte automaticamente.

## Rodando o Projeto

### 1. Clone o repositório

Primeiro, clone o repositório para a sua máquina:

```bash
git clone https://github.com/seu-usuario/tarefas-api.git
```

### 2. Suba os containers com o Docker Compose

#### Utilize o Docker Compose para criar e iniciar os containers:

docker-compose up --build

Esse comando irá construir os containers a partir do Dockerfile, configurar o banco de dados PostgreSQL e inicializar o servidor Django na porta 8000.
### 3. Acessando a API

A API estará rodando em http://localhost:8000. Você pode começar a fazer requisições HTTP para as rotas definidas no seu projeto.

### 4 Acessando a documentação da API

Este projeto inclui Swagger e Redoc para documentação interativa da API. 

    Swagger: http://localhost:8000/api/schema/swagger-ui/

    Redoc: http://localhost:8000/api/schema/redoc/

### 5. Executando comandos do Django no Docker

Caso precise rodar comandos de gerenciamento do Django (como migrações, shell, etc.), use o seguinte comando:

``` docker-compose exec web python manage.py <comando> ```

Exemplo para rodar as migrações:

``` docker-compose exec web python manage.py migrate ```


### 6. Testando a API

Para rodar os testes unitários, basta usar o comando: 

```docker-compose exec web python manage.py test```

### 7. Usando a API

Para usar a API, você pode usar ferramentas como Postman, Insomnia, etc. 

#### Rotas da API

A API possui as seguintes rotas para gerenciamento de tarefas:

**GET** /tasks/ - Retorna todas as tarefas no banco de dados.

**POST** /tasks/ - Cria uma nova tarefa. Exemplo de corpo da requisição:

```json
    {
      "id": 17,
      "titulo": "Comprar azeite",
      "descricao": "Comprar azeite no mercado",
      "prazo": "2024-03-28",
      "data_conclusao": null,
      "situacao": "nova"
    }
```

**GET** /tasks/{id}/ - Retorna os detalhes de uma tarefa específica.

**PATCH** /tasks/{id}/ - Atualiza uma tarefa existente.

**DELETE** /tasks/{id}/ - Deleta uma tarefa específica.

## Populando o Banco de Dados

Para rodar o comando que popula o banco de dados com dados fictícios, use o seguinte comando:

```bash 
docker-compose exec web python manage.py populate_db
```  
Este comando irá preencher o banco de dados com algumas tarefas de exemplo para facilitar os testes e a visualização da API.
Estrutura do Projeto

## Comandos Úteis

Subir containers: ```docker-compose up --build```

Parar containers: ```docker-compose down```

Rodar migrações: ```docker-compose exec web python manage.py migrate```

Acessar o shell do Django: ```docker-compose exec web python manage.py shell```

Rodar testes: ```docker-compose exec web python manage.py test```

Popular banco de dados: ```docker-compose exec web python manage.py populatedb```
