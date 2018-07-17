from models.database import db
from models.user import User
from . import routes
import json
from flask import request, abort, Response


@routes.route('/user/getAll', methods=['GET'])
def get_all():
    all_users = User.query.all()
    users_to_dict = []

    for user in all_users:
        user_dict = {
            'username': user.username,
            'email': user.email
        }
        users_to_dict.append(user_dict)

    return json.dumps(users_to_dict)


@routes.route('/user/<user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user_dict = User.query.get(user_id)
    print(user_dict.username)
    # user = User(user_dict['username'], user_dict['email'])
    # return str(user)
    return str(user_dict)


@routes.route('/user', methods=['POST'])
def post_user():
    user = User()
    if not request.json or not ('username' or 'email') in request.json:
        abort(400)
    else:
        user = User(request.json['username'], request.json['email'])
        print(str(user))
        db.session.add(user)
        db.session.commit()
    return Response(json.dumps(str(user)), mimetype='application/json')
