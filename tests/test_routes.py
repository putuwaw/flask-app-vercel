from flask import Flask
from handlers.routes import configure_routes


def test_index():
    app = Flask(__name__, template_folder="../templates")
    configure_routes(app)
    app.testing = True
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
