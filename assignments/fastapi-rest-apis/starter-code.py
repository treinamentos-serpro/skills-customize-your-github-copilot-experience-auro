from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Tasks API")


class Task(BaseModel):
    title: str
    completed: bool = False


# Coleção temporária para os exercícios.
tasks: dict[int, Task] = {}
next_task_id = 1


@app.get("/")
def read_root():
    return {"message": "Tasks API is running"}


@app.get("/tasks")
def list_tasks():
    return tasks


@app.post("/tasks", status_code=201)
def create_task(task: Task):
    global next_task_id
    task_id = next_task_id
    tasks[task_id] = task
    next_task_id += 1
    return {"id": task_id, **task.model_dump()}


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    task = tasks.get(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"id": task_id, **task.model_dump()}


# Implemente PUT /tasks/{task_id} e DELETE /tasks/{task_id} como parte da tarefa.
