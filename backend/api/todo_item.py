from flask import request, jsonify
from backend.api import bp
from backend.todo_item.repository import get_all_todos

@bp.route('/todo_item', methods=['GET'])
def get_todos():
    todo_items = get_all_todos()
    return jsonify(todo_items)


@bp.route('/todos', methods=['POST'])
def add_todo():
    data = request.get_json()
    new_todo = {"id": len(todos) + 1, "text": data.get("text"), "completed": False}
    todos.append(new_todo)
    return jsonify(new_todo), 201


@bp.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    data = request.get_json()
    for todo in todos:
        if todo["id"] == todo_id:
            todo["text"] = data.get("text", todo["text"])
            todo["completed"] = data.get("completed", todo["completed"])
            return jsonify(todo)
    return jsonify({"error": "Todo not found"}), 404



@bp.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [todo for todo in todos if todo["id"] != todo_id]
    return jsonify({"message": "Todo deleted successfully"})