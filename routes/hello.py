from . import routes


@routes.route('/', methods=['GET'])
def hello():
    return 'Hello World!'
