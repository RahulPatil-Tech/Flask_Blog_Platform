from flask_jwt_extended import get_jwt_identity
from functools import wraps
from flask import jsonify

def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        user = get_jwt_identity()
        if user['role'] != 'admin':
            return jsonify ({'msg': 'Admin access required'}), 403
        return fn(*args, **kwargs)
    return wrapper