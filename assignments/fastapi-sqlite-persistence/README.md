# 📘 Atividade: Persistência de Dados com SQLite e FastAPI

## 🎯 Objetivo

Aprenda a conectar uma API REST criada com FastAPI a um banco de dados SQLite, persistindo tarefas entre execuções e implementando operações CRUD com validação de dados.

## 📝 Tarefas

### 🛠️ Configurar o banco de dados SQLite

#### Descrição

Complete a configuração do banco SQLite e crie a tabela que armazenará as tarefas da API.

#### Requisitos

O programa concluído deve:

- Criar ou abrir um arquivo de banco SQLite.
- Criar uma tabela `tasks` quando ela ainda não existir.
- Armazenar um identificador, o título e o status de conclusão de cada tarefa.
- Manter os dados disponíveis após reiniciar a aplicação.

### 🛠️ Persistir tarefas pela API

#### Descrição

Implemente os endpoints da API para criar e consultar tarefas armazenadas no SQLite.

#### Requisitos

O programa concluído deve:

- Disponibilizar `POST /tasks` para inserir uma nova tarefa.
- Disponibilizar `GET /tasks` para listar as tarefas salvas.
- Disponibilizar `GET /tasks/{task_id}` para consultar uma tarefa pelo identificador.
- Usar modelos Pydantic para validar os dados recebidos.
- Retornar o status HTTP `404` quando a tarefa não existir.

### 🛠️ Atualizar e remover dados

#### Descrição

Adicione as operações restantes do CRUD e trate corretamente os casos em que o recurso não existe.

#### Requisitos

O programa concluído deve:

- Disponibilizar `PUT /tasks/{task_id}` para atualizar uma tarefa.
- Disponibilizar `DELETE /tasks/{task_id}` para remover uma tarefa.
- Usar consultas parametrizadas para inserir e alterar dados com segurança.
- Retornar respostas JSON com os dados da tarefa atualizada ou removida.
- Permitir testar todos os endpoints pela documentação interativa em `/docs`.

Exemplo de requisição para criar uma tarefa:

```json
{
  "title": "Estudar persistência com SQLite",
  "completed": false
}
```
