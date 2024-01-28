from backend.todo_item.model import TodoItem
from backend.database.database import db


def get_todo_items(page_size, current_page):
    start_index = (current_page - 1) * page_size
    todos = TodoItem.query.offset(start_index).limit(page_size).all()
    return [
        {
            "id": todo.id,
            "title": todo.title,
            "completed": todo.completed,
            "end_time": todo.end_time,
        }
        for todo in todos
    ]


def add_todo(title, completed=False):
    new_todo = TodoItem(title=title, completed=completed)
    db.session.add(new_todo)
    db.session.commit()
    return {"id": new_todo.id, "title": new_todo.title, "completed": new_todo.completed}


def update_todo(todo_id, title=None, completed=None):
    todo = TodoItem.query.get(todo_id)
    if todo:
        todo.title = title if title is not None else todo.text
        todo.completed = completed if completed is not None else todo.completed
        db.session.commit()
        return {"id": todo.id, "title": todo.title, "completed": todo.completed}
    return None


def delete_todo(todo_id):
    todo = TodoItem.query.get(todo_id)
    if todo:
        db.session.delete(todo)
        db.session.commit()
        return True
    return False


def get_todo_count():
    # 查询数据库获取TODO项的总数
    total_count = TodoItem.query.count()
    return total_count


def get_todo_by_id(todo_id):
    return TodoItem.query.get(todo_id)


def get_todo_items_by_page(current_page, page_size):
    return TodoItem.query.paginate(current_page, page_size, error_out=False)


def get_todo_items_by_completed(current_page, page_size, completed):
    return TodoItem.query.filter(TodoItem.completed == completed).paginate(current_page, page_size, error_out=False)
