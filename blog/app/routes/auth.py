from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required
from app.models.user import User
from flask_login import login_user
from app import db # Assuming 'db' is your SQLAlchemy instance

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            login_user(user)
            flash('Logged in successfully.', 'success')
            return redirect(url_for('main.index'))

        flash('Invalid email or password.', 'danger')
    return render_template('login.html')


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.login'))

@auth_bp.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form.get('email')
        # Here, you would usually check if the email exists and send a reset link.
        flash('If your email is registered, a reset link has been sent.', 'info')
        return redirect(url_for('auth.login'))
    
    return render_template('forgot_password.html')


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # --- ADD THESE PRINT STATEMENTS HERE ---
        print(f"DEBUG: Full request.form content: {request.form}")
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        print(f"DEBUG: Retrieved username: '{username}' (type: {type(username)})")
        print(f"DEBUG: Retrieved email: '{email}' (type: {type(email)})")
        print(f"DEBUG: Retrieved password (first 5 chars): '{password[:5] if password else 'N/A'}'")


        # --- ADDED VALIDATION HERE ---
        if not username:
            flash('Username is required.', 'danger')
            return redirect(url_for('auth.register'))
        
        if not email:
            flash('Email is required.', 'danger')
            return redirect(url_for('auth.register'))

        if not password:
            flash('Password is required.', 'danger')
            return redirect(url_for('auth.register'))

        # Validation (prevent duplicate users by email)
        if User.query.filter_by(email=email).first():
            flash('Email is already registered.', 'warning')
            return redirect(url_for('auth.register'))
        
        # Optional: Validate username uniqueness if desired
        if User.query.filter_by(username=username).first():
            flash('Username is already taken. Please choose another.', 'warning')
            return redirect(url_for('auth.register'))


        user = User(username=username, email=email) 
        user.set_password(password) # Assuming set_password hashes the password
        db.session.add(user)
        db.session.commit()

        flash('Account created successfully. Please log in.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html')