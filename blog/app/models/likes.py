# app/models/like.py
from app.extensions import db
from datetime import datetime

class Like(db.Model):
    """
    Represents a 'like' on a post by a user.
    Ensures that a user can only like a specific post once.
    """
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Add a unique constraint to ensure a user can only like a post once
    __table_args__ = (db.UniqueConstraint('user_id', 'post_id', name='_user_post_uc'),)

    # Relationships
    user = db.relationship('User', backref=db.backref('user_likes', lazy=True))
    # Renamed backref to 'associated_likes' to avoid conflict with 'likes_relationship' in Post
    post = db.relationship('Post', backref=db.backref('associated_likes', lazy='dynamic', cascade="all, delete-orphan"))

    def __init__(self, user_id, post_id) -> None:
        self.user_id = user_id
        self.post_id = post_id
    def __repr__(self):
        return f"<Like user_id={self.user_id} post_id={self.post_id}>"
