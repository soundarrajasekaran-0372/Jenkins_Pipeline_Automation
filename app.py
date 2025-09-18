from flask import Flask
import os

app = Flask(__name__)

@app.route("/")

def home():
    app_name = os.getenv("APP_NAME", "Default_App")
    return f"<h1>Hello from {app_name}!</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
