# app/routes/profile.py

from flask import Blueprint, render_template
from flask_login import login_required, current_user

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/profile')
@login_required  # Optional: restrict to logged-in users
def view_profile():
    return render_template('profile.html', user=current_user)
