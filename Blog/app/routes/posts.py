from flask import Blueprint, request, jsonify, redirect, render_template, url_for
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_login import login_required, current_user
from app.extensions import db
from app.models.post import Post
from app.models.user import User

post_bp = Blueprint('posts', __name__, url_prefix='/posts')


# GET all posts (API response)
@post_bp.route('/', methods=['GET'])
def get_all_post():
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return jsonify([
        {
            'id': post.id,
            'title': post.title,
            'content': post.content,
            'author': post.author.username if post.author else None,
            'likes': post.likes,
            'created_at': post.created_at.isoformat()
        } for post in posts
    ]), 200

@post_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        new_post = Post(title=title, content=content, author_id=current_user.id)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('create_post.html')


@post_bp.route('/<int:post_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    if current_user.id != post.author_id:
        return redirect(url_for('main.index'))

    if request.method == 'POST':
        post.title = request.form['title']
        post.content = request.form['content']
        db.session.commit()
        return redirect(url_for('main.view_post', post_id=post.id))

    return render_template('edit_post.html', post=post)



@post_bp.route('/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post_ui(post_id):
    post = Post.query.get_or_404(post_id)
    if current_user.id != post.author_id:
        return redirect(url_for('main.index'))

    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('main.index'))


@post_bp.route('/<int:post_id>/like', methods=['POST'])
@jwt_required()
def like_post(post_id):
    post = Post.query.get_or_404(post_id)
    post.likes += 1 
    db.session.commit()
    return jsonify({'msg': 'Post Liked', 'likes': post.likes}), 200
