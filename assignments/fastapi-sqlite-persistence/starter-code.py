import sqlite3
from contextlib import closing

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

DATABASE = "tasks.db"
app = FastAPI(title="Persistent Tasks API")


class TaskInput(BaseModel):
    title: str
    completed: bool = False


class Task(TaskInput):
    id: int


def get_connection() -> sqlite3.Connection:
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database() -> None:
    with closing(get_connection()) as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                completed INTEGER NOT NULL DEFAULT 0
            )
            """
        )
        connection.commit()


initialize_database()


@app.get("/")
def read_root():
    return {"message": "Persistent Tasks API is running"}


@app.get("/tasks", response_model=list[Task])
def list_tasks():
    raise NotImplementedError("Implement the task listing query")


@app.post("/tasks", response_model=Task, status_code=201)
def create_task(task: TaskInput):
    raise NotImplementedError("Implement the task insertion query")


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    raise NotImplementedError("Implement the task lookup query")


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task: TaskInput):
    raise NotImplementedError("Implement the task update query")


@app.delete("/tasks/{task_id}", response_model=Task)
def delete_task(task_id: int):
    raise NotImplementedError("Implement the task deletion query")
