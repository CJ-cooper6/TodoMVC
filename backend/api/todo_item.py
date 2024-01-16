from flask import request, jsonify
from backend.api import bp
from backend.todo_item.repository import get_all_todos, add_todo, update_todo, delete_todo
from flask_login import login_required

@login_required
@bp.route('/todos', methods=['GET'])
def get_todos():
    todo_items = get_all_todos()
    return jsonify(todo_items)

@login_required
@bp.route('/todos', methods=['POST'])
def add_todo_item():
    data = request.get_json()
    new_todo = add_todo(title=data.get("title"), completed=data.get("completed", False))
    return jsonify(new_todo), 200


@bp.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo_item(todo_id):
    data = request.get_json()
    updated_todo = update_todo(todo_id, title=data.get("title"), completed=data.get("completed"))
    if updated_todo:
        return jsonify(updated_todo)
    return jsonify({"error": "Todo not found"}), 404



@bp.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo_item(todo_id):
    result = delete_todo(todo_id)
    if result:
        return jsonify({"message": "Todo deleted successfully"})
    return jsonify({"error": "Todo not found"}), 404