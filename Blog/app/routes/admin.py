from flask import Blueprint, jsonify, request, render_template
from flask_jwt_extended import jwt_required
from app.models.user import User
from app.models.post import Post
from app.models.comment import Comment
from app.extensions import db
from app.utils.decorators import admin_required

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/delete_post/<int:post_id>', methods=['DELETE'])
@jwt_required()
@admin_required
def admin_delete_post(post_id):
    """
    Deletes a post by its ID.
    Requires JWT authentication and admin role.
    """
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return jsonify({'msg': 'Post deleted by admin'}), 200

@admin_bp.route('/delete_comment/<int:comment_id>', methods=['DELETE'])
@jwt_required()
@admin_required
def admin_delete_comment(comment_id):
    """
    Deletes a comment by its ID.
    Requires JWT authentication and admin role.
    """
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
    """
    Promotes a user to an admin role.
    Requires JWT authentication and admin role.
    """
    user = User.query.get_or_404(user_id)
    user.role = 'admin'
    db.session.commit()
    return jsonify({'msg': f'{user.username} promoted to admin'}), 200

@admin_bp.route('/dashboard')
@jwt_required()
@admin_required
def admin_dashboard():
    """
    Renders the admin dashboard page.
    Fetches all users and posts from the database.
    Requires JWT authentication and admin role.
    """
    users = User.query.all()
    posts = Post.query.all()
    return render_template('admin_dashboard.html', users=users, posts=posts)
