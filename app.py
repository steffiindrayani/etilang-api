from config import Config
from app import app, db

def create_tables():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    create_tables()
    app.secret_key=Config.SECRET_KEY
    app.run(host='0.0.0.0', port=8087)
