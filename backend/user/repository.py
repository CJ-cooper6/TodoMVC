from backend.user.model import User

def get_user_by_username(username):
   return User.query.filter_by(username=username).first()

def get_user(user_id):
   return User.query.filter_by(id=user_id).first()
