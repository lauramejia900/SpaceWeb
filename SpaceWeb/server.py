from flask_app import app
from flask_app.controllers import user_controller, likes_controllers, favorite_controller, comments_controller, events_controller


if __name__ == "__main__":
    app.run(debug=True)