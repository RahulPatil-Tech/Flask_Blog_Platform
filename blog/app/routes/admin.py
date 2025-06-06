from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.models.user import User
from app.models.post import Post
from app.models.comment import Comment
from app import db
from app.utils.decorators import admin_required

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/delete_post/<int:post_id>', methods=['DELETE'])
@jwt_required()
@admin_required
def admin_delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return jsonify({'msg': 'Post deleted by admin'}), 200

@admin_bp.route('/delete_comment/<int:comment_id>', methods=['DELETE'])
@jwt_required()
@admin_required
def admin_delete_comment(comment_id):  # 🔧 Fix: route name and function logic mismatch
    comment = Comment.query.get_or_404(comment_id)
    db.session.delete(comment)
    db.session.commit()
    return jsonify({'msg': 'Comment deleted by admin'}), 200

@admin_bp.route('/users', methods=['GET'])
@jwt_required()
@admin_required
def get_all_users():
    users = User.query.all()
    return jsonify([{
        'id': u.id,
        'username': u.username,
        'email': u.email,
        'role': u.role
    } for u in users]), 200

@admin_bp.route('/promote/<int:user_id>', methods=['PUT'])
@jwt_required()
@admin_required
def promote_user(user_id):
    user = User.query.get_or_404(user_id)
    user.role = 'admin'
    db.session.commit()
    return jsonify({'msg': f'{user.username} promoted to admin'}), 200
