from backend.user.model import User

def get_user_by_username(username):
   return User.query.filter_by(username=username).first()
