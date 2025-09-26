from flask import Flask

def create_app():
    app = Flask(__name__)

    from .routes import bp
    app.register_blueprint(bp)

    return app

# For `flask run`
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
