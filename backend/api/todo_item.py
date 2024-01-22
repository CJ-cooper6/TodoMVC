from flask import request, jsonify
from backend.api import bp
from backend.todo_item.repository import get_todo_items, add_todo, update_todo, delete_todo, get_todo_count
from flask_login import login_required
from backend.todo_item.service import changeTodoStatusById


@login_required
@bp.route('/todos', methods=['GET'])
def get_todos():
    page_size = int(request.args.get('pageSize', 10))
    current_page = int(request.args.get('currentPage', 1))
    print("page_size:", page_size)
    print("current_page:", current_page)
    total = get_todo_count()
    todo_items = get_todo_items(page_size, current_page)
    return jsonify({"total": total, "todo_items": todo_items})


@login_required
@bp.route('/todos', methods=['POST'])
def add_todo_item():
    data = request.get_json()
    new_todo = add_todo(title=data.get("title"), completed=data.get("completed", False))
    return jsonify(new_todo), 200


@login_required
@bp.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo_item(todo_id):
    data = request.get_json()
    updated_todo = update_todo(todo_id, title=data.get("title"), completed=data.get("completed"))
    if updated_todo:
        return jsonify(updated_todo)
    return jsonify({"error": "Todo not found"}), 404


@login_required
@bp.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo_item(todo_id):
    result = delete_todo(todo_id)
    if result:
        return jsonify({"message": "Todo deleted successfully"})
    return jsonify({"error": "Todo not found"}), 404


@login_required
@bp.route('/todos/<int:todo_id>', methods=['POST'])
def changeTodoStatus(todo_id):
    data = request.get_json()
    status = data.get("todoStatus")

    result = changeTodoStatusById(todo_id, status)
    if result:
        return jsonify({"status": "ok"}), 200

    return jsonify({"error": "change Todo Status error"}), 404
