from flask import request
from backend.api import bp
from backend.todo_item.repository import (
    add_todo,
    update_todo,
    delete_todo,
    get_todo_items_by_page,
    get_todo_items_by_completed,
)
from flask_login import login_required
from backend.todo_item.service import changeTodoStatusById
from backend.response_helper import success, bad_request_with_data
from backend.request_helper import get_pagination


@bp.route("/todos", methods=["GET"])
@login_required
def get_todos():
    current_page, page_size = get_pagination()
    todos = get_todo_items_by_page(current_page, page_size)
    serialized_todos = [todo.to_dict() for todo in todos.items]
    return success({"total": todos.total, "todo_items": serialized_todos})


@bp.route("/todos", methods=["POST"])
@login_required
def add_todo_item():
    data = request.get_json()
    new_todo = add_todo(title=data.get("title"), completed=data.get("completed", False))
    return success({"new_todo": new_todo})


@bp.route("/todos/<int:todo_id>", methods=["PUT"])
@login_required
def update_todo_item(todo_id):
    data = request.get_json()
    updated_todo = update_todo(todo_id, title=data.get("title"), completed=data.get("completed"))
    if updated_todo:
        return success({"updated_todo": updated_todo})
    return bad_request_with_data({"error": "Todo not found"}, 404)


@bp.route("/todos/<int:todo_id>", methods=["DELETE"])
@login_required
def delete_todo_item(todo_id):
    result = delete_todo(todo_id)
    if result:
        return success({"message": "Todo deleted successfully"})
    return bad_request_with_data({"error": "Todo not found"}, 404)


@bp.route("/todos/<int:todo_id>", methods=["POST"])
@login_required
def changeTodoStatus(todo_id):
    data = request.get_json()
    status = data.get("todoStatus")

    result = changeTodoStatusById(todo_id, status)
    if result:
        return success({"status": "ok"})

    return bad_request_with_data({"error": "change Todo Status error"}, 404)


@bp.route("/todos/status", methods=["GET"])
@login_required
def get_finished_todos():
    completed = request.args.get("completed", True)
    current_page, page_size = get_pagination()
    todos = get_todo_items_by_completed(current_page, page_size, completed)
    serialized_todos = [todo.to_dict() for todo in todos.items]
    return success({"total": todos.total, "todo_items": serialized_todos})
