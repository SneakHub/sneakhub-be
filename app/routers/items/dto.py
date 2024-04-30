from ...schemas.item import BaseItem, Item


# Data Transfer Objects (DTOs)
class CreateItemRequest(BaseItem):
    pass


class UpdateItemRequest(Item):
    pass
