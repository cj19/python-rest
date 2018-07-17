from flask import Flask

from models.database import db
from models.user import User
from routes import routes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:asdasdasd@localhost/postgres'
app.register_blueprint(routes)

db.app = app
db.init_app(app)

if __name__ == '__main__':
    db.create_all()
    # db.session.add(User('admin', 'darvas.roland@gmail.com'))
    # db.session.commit()
    app.run(host='0.0.0.0', port=5000)
