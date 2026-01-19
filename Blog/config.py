import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "this-should-be-secret-and-random")

    # Use Railway TCP Proxy for external DB access
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://root:{os.getenv('DB_PASSWORD')}@"
        f"{os.getenv('RAILWAY_TCP_PROXY_DOMAIN')}:{os.getenv('RAILWAY_TCP_PROXY_PORT')}/railway"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask-Mail settings
    MAIL_SERVER = "smtp.gmail.com"      
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = ("FlaskBlog", os.getenv("MAIL_USERNAME"))

    # SSL options for secure connection
    SQLALCHEMY_ENGINE_OPTIONS = {
        "connect_args": {"ssl": {}}
    }
