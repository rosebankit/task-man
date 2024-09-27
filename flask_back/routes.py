# project/flask_back/Routes/views.py


from flask import Blueprint, render_template

route_blueprint = Blueprint("route", __name__)

@route_blueprint.route("/task")
def example_route():
    return "<h1>Task</h1>"

@route_blueprint.route('/handler')
def example_template_route():
    return render_template('handler.html')

@route_blueprint.route("/jwt")
@jwt_auth(return_user_id=True)
def example_route_with_jwt(user_id):
    return 'hello world route with user_id: {0}'.format(user_id)

@route_blueprint.route('/jwtindex')
@jwt_auth()
def example_template_route_with_jwt():
    return render_template('index.html')