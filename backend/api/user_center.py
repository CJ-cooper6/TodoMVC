from flask_login import login_required
from backend.response_helper import success, bad_request_with_data
from backend.user.repository import get_user
from backend.user.service import update_user
from flask_login import current_user
from backend.api import bp
from flask import request



@bp.route("/user", methods=["GET"])
@login_required
def get_user_info():
    print("current_user.id:", current_user.id)
    user = get_user(current_user.id)
    serialized_user = user.to_dict()
    return success(serialized_user)



@bp.route("/user", methods=["PUT"])
@login_required
def update_user_info():
    data = request.get_json()
    user_id = current_user.id
    result = update_user(user_id, data)
    if result:
        return success({"message": "success"})
    return bad_request_with_data({"message": "update failed!"})