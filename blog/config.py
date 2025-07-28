class Config:
    SECRET_KEY = 'this-should-be-secret-and-random'

    # URL-encoded password: '@' becomes '%40'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://rp32:Strong%40123@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
