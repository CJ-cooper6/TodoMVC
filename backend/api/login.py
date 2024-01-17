from flask import request, jsonify
from backend.api import bp
from backend.user.repository import get_user_by_username
from flask_login import login_user

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

   