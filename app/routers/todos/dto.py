from ...schemas.todos import BaseToDos, ToDos


# Data Transfer Objects (DTOs)
class CreateToDosRequest(BaseToDos):
    pass


class UpdateToDosRequest(ToDos):
    pass
