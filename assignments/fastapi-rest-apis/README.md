# 📘 Atividade: Building REST APIs com FastAPI

## 🎯 Objetivo

Aprenda a criar uma API REST com o framework FastAPI, definindo endpoints HTTP, validando dados com modelos Pydantic e documentando automaticamente os recursos da aplicação.

## 📝 Tarefas

### 🛠️ Configurar a API FastAPI

#### Descrição

Complete a configuração inicial do projeto e crie um endpoint de boas-vindas para confirmar que a API está funcionando.

#### Requisitos

O programa concluído deve:

- Criar uma instância do FastAPI.
- Disponibilizar uma rota `GET /`.
- Retornar uma resposta JSON com uma mensagem de boas-vindas.
- Permitir a execução da aplicação com Uvicorn.

### 🛠️ Criar endpoints de tarefas

#### Descrição

Implemente uma API para cadastrar e consultar tarefas usando uma coleção em memória.

#### Requisitos

O programa concluído deve:

- Disponibilizar `GET /tasks` para listar todas as tarefas.
- Disponibilizar `POST /tasks` para criar uma tarefa.
- Disponibilizar `GET /tasks/{task_id}` para consultar uma tarefa pelo identificador.
- Retornar o status HTTP `404` quando a tarefa solicitada não existir.
- Usar um modelo Pydantic com título e status de conclusão.

### 🛠️ Atualizar e remover tarefas

#### Descrição

Adicione operações para alterar o status de uma tarefa e removê-la da coleção.

#### Requisitos

O programa concluído deve:

- Disponibilizar `PUT /tasks/{task_id}` para atualizar os dados de uma tarefa.
- Disponibilizar `DELETE /tasks/{task_id}` para remover uma tarefa.
- Validar os dados recebidos antes de processá-los.
- Retornar respostas JSON claras para operações concluídas.
- Permitir consultar a documentação interativa em `/docs`.

Exemplo de requisição para criar uma tarefa:

```json
{
  "title": "Estudar FastAPI",
  "completed": false
}
```
