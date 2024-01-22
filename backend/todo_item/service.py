from backend.todo_item.repository import get_todo_by_id
from backend.database.database import db


def changeTodoStatusById(todo_id, status):
    todo = get_todo_by_id(todo_id)
    print(todo)
    if todo:
        todo.completed = status
        db.session.add(todo)
        db.session.commit()
        return True
    return False
