Flask-CRUD
=========

User management architecture for a Flask application.

Installation (Development Mode) / You can skip this step if you just want to test the app
-------------------------------

1. Clone the git repository and navigate to the root of the project.
2. Install [Poetry](https://python-poetry.org/) using the following command:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```
3. Create a virtual environment using Poetry:
```
poetry shell
```
4. Install dependencies using Poetry:
```
poetry install
```
Launching
---------

1. Build and launch the database using the following command:
```bash
docker-compose up -d --build flask_db
```
2. Build and launch the application using the following command:
```bash
docker-compose up --build flask_app
```
The application will be accessible at the following address: <http://localhost:5000>.

Stopping
--------

To stop the application and the database, use the following command:
```
docker-compose down
```
This will stop all running containers and remove associated networks.

Remarques
------------

End-points testing

For VS Code users, you can directly import [collection](tests/postman/Flask-CRUD.postman_collection.json) in [Postman](https://marketplace.visualstudio.com/items?itemName=Postman.postman-for-vscode)

Contribution
------------

Contributions are welcome! If you would like to contribute to this project, please open a pull request.

License
-------

This project is licensed under the MIT license. See the `LICENSE` file for more details.