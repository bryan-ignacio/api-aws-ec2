from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__)

    @app.get("/")
    def hello_world():
        return "Hola Mundo"

    return app


app = create_app()


if __name__ == "__main__":
    # Run the development server
    app.run(host="0.0.0.0", port=5001, debug=True)
