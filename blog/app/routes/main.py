from flask import Blueprint, request, render_template
from app.models.post import Post
from app.extensions import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    search = request.args.get('q', '', type=str)

    query = Post.query.order_by(Post.created_at.desc())

    if search:
        query = query.filter(Post.title.ilike(f"%{search}%")) #type: ignore

    posts = query.paginate(page=page, per_page=5)

    return render_template('index.html', posts=posts, search=search)

@main_bp.route('/post/<int:post_id>')
def view_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('view_post.html', post=post)
