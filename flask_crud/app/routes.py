from flask import request, jsonify, Response
from http import HTTPStatus
from flask_crud.app import app, db
from .models import User


@app.route('/users', methods=['POST'])
def create_user() -> Response:
    """
    Create a new user.

    Method: POST
    Endpoint: /users

    This function creates a new user using the JSON data provided in the request.
    It extracts the data from the JSON body of the request, creates a new User object with this data,
    adds it to the database session, and commits the changes.
    If an error occurs, it returns a response with an HTTP status code 500.
    """
    try:
        data = request.get_json()
        new_user = User(first_name=data['first_name'], last_name=data['last_name'],
                        username=data['username'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()

        return {'message': 'User created'}, HTTPStatus.CREATED
    except Exception as e:
        return {'message': f'Error creating user {e}'}, HTTPStatus.INTERNAL_SERVER_ERROR


@app.route('/users', methods=['GET'])
def get_users() -> Response:
    """
    Get all users.

    Method: GET
    Endpoint: /users

    This function retrieves all users from the database and returns a JSON response containing a list of users.
    If an error occurs, it returns a response with an HTTP status code 500.
    """
    try:
        users = [user.to_json() for user in User.query.all()]
        return {'users': users}, HTTPStatus.OK
    except Exception as e:
        return {'message': f'Error while getting users {e}'}, HTTPStatus.INTERNAL_SERVER_ERROR


@app.route('/users/<int:id>', methods=['GET'])
def get_user(id: int) -> Response:
    """
    Get a user by ID.

    Method: GET
    Endpoint: /users/<id>

    This function retrieves a specific user from the database using the ID provided in the URL.
    If the user is found, it is returned as a JSON object.
    Otherwise, a response with an HTTP status code 404 is returned to indicate that the user is not found.
    If an error occurs, it returns a response with an HTTP status code 500.
    """
    try:
        user = User.query.filter_by(id=id).first()
        if user:
            return jsonify({'user': user.to_json()}), HTTPStatus.OK
        return {'message': 'User not found'}, HTTPStatus.NOT_FOUND
    except Exception as e:
        return {'message': f'Error while getting user {e}'}, HTTPStatus.INTERNAL_SERVER_ERROR


@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id: int) -> Response:
    """
    Update a user by ID.

    Method: PUT
    Endpoint: /users/<id>

    This function updates the information of a specific user using the ID provided in the URL
    and the JSON data provided in the request body.
    If the user is found, their information is updated with the new data and the changes are committed.
    If an error occurs, it returns a response with an HTTP status code 500.
    """
    try:
        user: User = User.query.filter_by(id=id).first()
        if user:
            data = request.get_json()
            user.first_name = data['first_name']
            user.last_name = data['last_name']
            user.username = data['username']
            user.email = data['email']
            db.session.commit()

            return {'message': 'User updated'}, HTTPStatus.OK
        return {'message': 'User not found'}, HTTPStatus.NOT_FOUND
    except Exception as e:
        return {'message': f'Error while updating user {e}'}, HTTPStatus.INTERNAL_SERVER_ERROR


@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id: int) -> Response:
    """
    Delete a user by ID.

    Method: DELETE
    Endpoint: /users/<id>

    This function deletes a specific user from the database using the ID provided in the URL.
    If the user is found, they are deleted from the database.
    If an error occurs, it returns a response with an HTTP status code 500.
    """
    try:
        user = User.query.filter_by(id=id).first()
        if user:
            db.session.delete(user)
            db.session.commit()

            return {'message': 'User deleted'}, HTTPStatus.OK
        return {'message': 'User not found'}, HTTPStatus.NOT_FOUND
    except Exception as e:
        return {'message': f'Error while deleting user {e}'}, HTTPStatus.INTERNAL_SERVER_ERROR
