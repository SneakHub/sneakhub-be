from datetime import datetime

from pydantic import BaseModel

from app.utils.factory import UUID4Factory, CurrentTimeFactory


class BaseToDos(BaseModel):
    title: str
    done: bool

class ToDos(UUID4Factory, CurrentTimeFactory, BaseToDos):
    @staticmethod
    def from_dict(source: BaseToDos):
        title = source.get('title')
        created_at = datetime.fromisoformat(source.get('created_at'))
        updated_at = datetime.fromisoformat(source.get('updated_at'))
        done = source.get('done')
        return ToDos(title=title, created_at=created_at, updated_at=updated_at, done=done)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'done': self.done
        }

    # def __repr__(self):
    #     return f"Todo(\
    #                   id={self.id},\
    #                   title={self.title}, \
    #                   created_at={self.created_at}, \
    #                   updated_at={self.updated_at}, \
    #                   done={self.done}\
    #               )"

