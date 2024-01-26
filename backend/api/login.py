from flask import request, jsonify
from backend.api import bp
from backend.user.repository import get_user_by_username
from flask_login import login_user, current_user

@bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username=data.get('username')
    password=data.get('password')
    print(username,password)
    user = get_user_by_username(username)
    if user and user.check_password(password):
        login_user(user, remember=True)
        return jsonify({"login": "success"}), 201

    return jsonify({"login": "fail"}), 500


@bp.route('/check-login-status', methods=["GET"])
def check_login_status():
    if current_user.is_authenticated:
        return jsonify({'status': 'success', 'message': '用户已登陆'})
    else:
        return jsonify({'status': 'error', 'message': '未登陆'}), 401