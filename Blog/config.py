import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "this-should-be-secret-and-random")

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://root:{os.getenv('DB_PASSWORD')}@"
        f"{os.getenv('RAILWAY_TCP_PROXY_DOMAIN')}:"
        f"{os.getenv('RAILWAY_TCP_PROXY_PORT')}/railway"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 🔥 CRITICAL FOR RAILWAY TCP PROXY
    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_pre_ping": True,      
        "pool_recycle": 120,        
        "pool_size": 5,
        "max_overflow": 5,
        "connect_args": {
            "ssl": {},
            "connect_timeout": 10,
            "read_timeout": 30,
            "write_timeout": 30,
        },
    }

    # Flask-Mail
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = ("FlaskBlog", os.getenv("MAIL_USERNAME"))
