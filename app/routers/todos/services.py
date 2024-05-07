# This file is to simulate the database operations
from datetime import datetime
from typing import List, Union

from google.cloud.firestore_v1 import DocumentSnapshot

from ... import firebase as repository
from ...schemas.todos import BaseToDos, ToDos
from ...utils.list import find

# Simulate as atodo database
todos: List[ToDos] = []

def snapshot_to_todo(snapshot: DocumentSnapshot) -> ToDos:
    data = snapshot.to_dict()

    # print(data); print(type(data['created_at']));
    return ToDos(
        title=data['title'],
        created_at=data['created_at'],
        updated_at=data['updated_at'],
        done=data['done'],
        id=data['id']
    )


def find_all() -> List[ToDos]:
    docs = repository.get_all_doc("todos")

    todos: List[ToDos] = []
    for doc in docs:
        todos = [*todos, snapshot_to_todo(doc)]

    return todos


def find_one(id: str) -> ToDos:
    todo = repository.find_doc("todos", id)
    if not todo:
        raise Exception(f"ToDos with id {id} not found")
    return snapshot_to_todo(todo)


def create_one(data: BaseToDos) -> ToDos:
    # global todos
    todo = ToDos(**data.dict())
    # Add the createdtodo to the database

    # todos = [*todos, todo]
    repository.add_doc("todos", todo)

    return todo


def delete_one(id: str) -> Union[None, ToDos]:
    # global todos
    # todo = find(lambda todo: todo.id == id, todos)
    # if not todo:
    #     return None
    # # Delete the existing atodo from the database
    # todos = list(filter(lambda todo: todo.id != id, todos))

    todo = repository.delete_doc("todos", id)
    if todo:
        return snapshot_to_todo(todo)
    return None


def update_one(id: str, data: ToDos) -> ToDos:
    # global todos
    # todo = find(lambda todo: todo.id == id, todos)
    # if not todo:
    #     raise Exception(f"ToDos with id {id} not found")
    # # Update the existing atodo
    # todos = list(map(lambda todo: data if todo.id == id else todo, todos))
    #return data

    todo = repository.update_doc("todos", id, data.to_dict())
    if not todo:
        raise Exception(f"document[${id}] is not found to update!")
    return snapshot_to_todo(todo)

