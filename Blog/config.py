import os
class Config:
    SECRET_KEY = 'this-should-be-secret-and-random'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:hNolfQXzqIDgNMJGpcoiQoPHXkxEKiKq@mysql.railway.internal:3306/railway'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask-Mail settings
    MAIL_SERVER = "smtp.gmail.com"      
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = ("FlaskBlog", os.getenv("MAIL_USERNAME"))
