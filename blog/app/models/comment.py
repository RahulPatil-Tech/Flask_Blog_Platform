from app.extensions import db
from datetime import datetime
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('comments', lazy=True))

    def __init__(self, post_id, content, user_id):
        self.post_id = post_id
        self.content = content
        self.user_id = user_id