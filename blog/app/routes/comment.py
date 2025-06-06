from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models.comment import Comment
from app.models.post import Post

comment_bp = Blueprint('comment', __name__, url_prefix='/comments')

# GET all comments for a post
@comment_bp.route('/<int:post_id>', methods=['GET'])
def get_comments(post_id):
    comments = Comment.query.filter_by(post_id=post_id).order_by(Comment.created_at.desc()).all()
    return jsonify([{
        'id': c.id,
        'content': c.content,
        'user_id': c.user_id,
        'created_at': c.created_at.isoformat()
    } for c in comments]), 200


# POST a comment to a post
@comment_bp.route('/<int:post_id>', methods=['POST'])
@jwt_required()
def add_comment(post_id):
    post = Post.query.get_or_404(post_id)
    
    user_identity = get_jwt_identity()
    if not isinstance(user_identity, dict) or 'id' not in user_identity:
        return jsonify({'msg': 'Unauthorized: Invalid token payload'}), 401
    
    data = request.get_json()
    content = data.get('content') if data else None
    
    if not content or not content.strip():
        return jsonify({'msg': 'Content cannot be empty'}), 400

    comment = Comment(content=content.strip(), user_id=user_identity['id'], post_id=post.id)
    
    db.session.add(comment)
    db.session.commit()
    
    return jsonify({'msg': 'Comment added successfully'}), 201

