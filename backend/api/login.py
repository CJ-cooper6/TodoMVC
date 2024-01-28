from flask import request
from backend.api import bp
from backend.user.repository import get_user_by_username
from flask_login import login_user, current_user, logout_user
from backend.response_helper import success, bad_request_with_data


@bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    print(username, password)
    user = get_user_by_username(username)
    if user and user.check_password(password):
        login_user(user, remember=True)
        return success({"login": "success"})

    return bad_request_with_data({"login": "fail"}, 500)


@bp.route("/check-login-status", methods=["GET"])
def check_login_status():
    if current_user.is_authenticated:
        return success({"status": "success", "message": "用户已登陆"})
    else:
        return bad_request_with_data({"status": "error", "message": "未登陆"}, 401)


@bp.route("/sign-out", methods=["POST"])
def sign_out():
    logout_user()
    return success({"message": "退出登陆成功"})
