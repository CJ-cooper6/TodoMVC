
from backend.todo_item.model import TodoItem
from backend.database.database import db


def get_all_todos():
    todos = TodoItem.query.all()
    return [{"id": todo.id, "text": todo.text, "completed": todo.completed} for todo in todos]


def add_todo(text, completed=False):
    new_todo = TodoItem(text=text, completed=completed)
    db.session.add(new_todo)
    db.session.commit()
    return {"id": new_todo.id, "text": new_todo.text, "completed": new_todo.completed}


def update_todo(todo_id, text=None, completed=None):
    todo = TodoItem.query.get(todo_id)
    if todo:
        todo.text = text if text is not None else todo.text
        todo.completed = completed if completed is not None else todo.completed
        db.session.commit()
        return {"id": todo.id, "text": todo.text, "completed": todo.completed}
    return None


def delete_todo(todo_id):
    todo = TodoItem.query.get(todo_id)
    if todo:
        db.session.delete(todo)
        db.session.commit()
        return True
    return False
