# app/routes/auth.py

from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required
from app.models.user import User
from app.extensions import db, mail
from flask_mail import Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
import os

auth_bp = Blueprint('auth', __name__)
s = URLSafeTimedSerializer(os.getenv('SECRET_KEY', 'default-secret-key'))


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
        user = User.query.filter_by(email=email).first()

        if user:
            token = s.dumps(user.email, salt='password-reset-salt')
            reset_url = url_for('auth.reset_password', token=token, _external=True)

            # Email message
            msg = Message('Password Reset Request', recipients=[user.email])
            msg.body = f'Your password reset link is: {reset_url}'
            msg.html = render_template('email/reset_password_email.html', reset_url=reset_url)

            mail.send(msg)

        flash('If an account with that email exists, a password reset link has been sent.', 'info')
        return redirect(url_for('auth.login'))
    
    return render_template('forgot_password.html')


@auth_bp.route('/reset-password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    try:
        email = s.loads(token, salt='password-reset-salt', max_age=3600)
    except SignatureExpired:
        flash('The password reset link has expired.', 'danger')
        return redirect(url_for('auth.forgot_password'))
    except:
        flash('The password reset link is invalid.', 'danger')
        return redirect(url_for('auth.forgot_password'))
    
    user = User.query.filter_by(email=email).first()
    if not user:
        flash('Invalid token or user not found.', 'danger')
        return redirect(url_for('auth.forgot_password'))
        
    if request.method == 'POST':
        new_password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if new_password != confirm_password:
            flash('Passwords do not match.', 'danger')
            return render_template('reset_password.html', token=token)

        user.set_password(new_password)
        db.session.commit()
        flash('Your password has been updated successfully.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('reset_password.html', token=token)


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        if not username:
            flash('Username is required.', 'danger')
            return redirect(url_for('auth.register'))
        
        if not email:
            flash('Email is required.', 'danger')
            return redirect(url_for('auth.register'))

        if not password:
            flash('Password is required.', 'danger')
            return redirect(url_for('auth.register'))

        if User.query.filter_by(email=email).first():
            flash('Email is already registered.', 'warning')
            return redirect(url_for('auth.register'))
        
        if User.query.filter_by(username=username).first():
            flash('Username is already taken. Please choose another.', 'warning')
            return redirect(url_for('auth.register'))

        user = User(username=username, email=email) 
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

        flash('Account created successfully. Please log in.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html')
