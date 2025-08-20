# app/models/post.py
from datetime import datetime
from app.extensions import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
    # REMOVED: likes = db.Column(db.Integer, default=0)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    author = db.relationship('User', backref=db.backref('posts', lazy=True))
    comments = db.relationship('Comment', backref='post', lazy='dynamic', cascade="all, delete-orphan")
    likes_relationship = db.relationship('Like', backref='post_liked_by_users', lazy='dynamic', cascade="all, delete-orphan")

    def __init__(self, title, content, author_id):
        self.title = title
        self.content = content
        self.author_id = author_id

    @property
    def likes_count(self):
        """Returns the total count of likes for this post."""
        return self.likes_relationship.count()

    @property
    def comments_count(self):
        """Returns the total count of comments for this post."""
        return self.comments.count()
