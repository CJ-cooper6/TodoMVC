from datetime import datetime
from backend.database import db


class TodoItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.String(255))
    completed = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    end_time = db.Column(db.DateTime)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "completed": self.completed,
            "user_id": self.user_id,
            "created_at": self.created_at,
            "end_time": self.end_time,
        }
