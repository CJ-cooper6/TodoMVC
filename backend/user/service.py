from backend.user.repository import get_user
from backend.database.database import db


def update_user(id, user_info):
    user = get_user(id)
    print("data:", user_info)
    print("user.__dict:", user.__dict__)
    if user:
        user.username = user_info['username']
        user.nickname = user_info['nickname']
        user.email = user_info['email']
        db.session.commit()
        return {"message": "ok"}
    return False