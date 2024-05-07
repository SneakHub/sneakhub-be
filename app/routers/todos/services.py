# This file is to simulate the database operations

from typing import List, Union

from ...schemas.todos import BaseToDos, ToDos
from ...utils.list import find

# Simulate as atodo database
todos: List[ToDos] = []


def find_all() -> List[ToDos]:
    return todos


def find_one(id: str) -> ToDos:
    todo = find(lambda todo: todo.id == id, todos)
    if not todo:
        raise Exception(f"ToDos with id {id} not found")
    return todo


def create_one(data: BaseToDos) -> ToDos:
    global todos
    todo = ToDos(**data.dict())
    # Add the createdtodo to the database
    todos = [*todos, todo]
    return todo


def delete_one(id: str) -> Union[None, ToDos]:
    global todos
    todo = find(lambda todo: todo.id == id, todos)
    if not todo:
        return None
    # Delete the existing atodo from the database
    todos = list(filter(lambda todo: todo.id != id, todos))
    return todo


def update_one(id: str, data: ToDos) -> ToDos:
    global todos
    todo = find(lambda todo: todo.id == id, todos)
    if not todo:
        raise Exception(f"ToDos with id {id} not found")
    # Update the existing atodo
    todos = list(map(lambda todo: data if todo.id == id else todo, todos))
    return data
