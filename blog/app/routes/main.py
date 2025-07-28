# app/routes/main.py
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.models.post import Post # Correct import
from app.models.comment import Comment # Correct import
from app.models.likes import Like # Correct import (assuming app/models/like.py)
from app.extensions import db # Your SQLAlchemy instance

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
@main_bp.route('/index')
def index():
        page = request.args.get('page', 1, type=int)
        search = request.args.get('q', type=str)

        if search:
            posts_query = Post.query.filter(
                (Post.title.ilike(f'%{search}%')) | (Post.content.ilike(f'%{search}%'))
            )
        else:
            posts_query = Post.query

        posts_query = posts_query.order_by(Post.created_at.desc())
        posts = posts_query.paginate(page=page, per_page=5, error_out=False)
        return render_template('index.html', posts=posts, search=search)

@main_bp.route('/post/<int:post_id>')
def view_post(post_id):
        post = Post.query.get_or_404(post_id)
        comments = post.comments.order_by(Comment.created_at.asc()).all()

        has_liked = False
        if current_user.is_authenticated:
            has_liked = Like.query.filter_by(user_id=current_user.id, post_id=post.id).first() is not None

        return render_template('post_detail.html',
                               post=post,
                               comments=comments,
                               has_liked=has_liked)

@main_bp.route('/like_post/<int:post_id>', methods=['POST'])
@login_required
def like_post(post_id):
        post = Post.query.get_or_404(post_id)
        existing_like = Like.query.filter_by(user_id=current_user.id, post_id=post.id).first()

        if existing_like:
            db.session.delete(existing_like)
            flash('Post unliked!', 'info')
        else:
            new_like = Like(user_id=current_user.id, post_id=post.id)
            db.session.add(new_like)
            flash('Post liked!', 'success')

        db.session.commit()
        return redirect(url_for('main.view_post', post_id=post.id))

@main_bp.route('/post/<int:post_id>/comment', methods=['POST'])
@login_required
def add_comment(post_id):
        post = Post.query.get_or_404(post_id)
        content = request.form.get('content')

        if not content:
            flash('Comment cannot be empty.', 'danger')
            return redirect(url_for('main.view_post', post_id=post.id))

        comment = Comment(content=content, user_id=current_user.id, post_id=post.id)
        db.session.add(comment)
        db.session.commit()
        flash('Comment added successfully!', 'success')
        return redirect(url_for('main.view_post', post_id=post.id))
    