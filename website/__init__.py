from flask import Flask

def create_app():
    app = Flask("__name__", template_folder="website/templates", static_folder="website/static")
    app.config['SECRET_KEY'] = "senha"

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app