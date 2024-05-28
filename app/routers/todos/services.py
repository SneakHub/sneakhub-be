# This file is to simulate the database operations
from datetime import datetime
from typing import List, Union

from google.cloud.firestore_v1 import DocumentSnapshot

from ... import firebase as repository
from ...schemas.todo import BaseTodo, ToDo
from ...utils.list import find

# Simulate as atodo database
todos: List[ToDo] = []


def snapshot_to_todo(snapshot: DocumentSnapshot) -> ToDo:
    data = snapshot.to_dict()

    # print(data); print(type(data['created_at']));
    response = ToDo(**data)

    return response


def snapshot_to_todo_Delete(snapshot: DocumentSnapshot, time: datetime) -> ToDo:
    data = snapshot.to_dict()
    data.__setattr__("updated_at", time)

    # print(data); print(type(data['created_at']));
    response = ToDo(**data)

    return response


def find_all() -> List[ToDo]:
    docs = repository.get_all_doc("todos")

    todos: List[ToDo] = []
    for doc in docs:
        todos = [*todos, snapshot_to_todo(doc)]

    return todos


def find_one(id: str) -> ToDo:
    todo = repository.find_doc("todos", id)
    if not todo:
        raise Exception(f"ToDo with id {id} not found")
    return snapshot_to_todo(todo)


def create_one(data: BaseTodo) -> ToDo:
    # global todos
    todo = ToDo(**data.dict())
    # Add the createdtodo to the database

    # todos = [*todos, todo]
    repository.add_doc("todos", todo)

    return todo


def delete_one(id: str) -> Union[None, ToDo]:
    # global todos
    # todo = find(lambda todo: todo.id == id, todos)
    # if not todo:
    #     return None
    # # Delete the existing atodo from the database
    # todos = list(filter(lambda todo: todo.id != id, todos))

    todo, t = repository.delete_doc("todos", id)
    if todo:
        return snapshot_to_todo_Delete(todo, t)
        # forget update the "updated_at" field!
    return None


def update_one(id: str, data: BaseTodo) -> ToDo:
    # global todos
    # todo = find(lambda todo: todo.id == id, todos)
    # if not todo:
    #     raise Exception(f"ToDo with id {id} not found")
    # # Update the existing atodo
    # todos = list(map(lambda todo: data if todo.id == id else todo, todos))
    # return data

    # print(data.to_dict())
    todo = repository.update_doc("todos", id, data.to_dict())
    if not todo:
        raise Exception(f"document[${id}] is not found to update!")
    return snapshot_to_todo(todo)
