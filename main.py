# importing flask
from flask import Flask

# create instance of Flask
app = Flask(__name__)
# route
@app.route("/")
def home():
    return "Hey Buddy, Welcome Home!"

@app.route("/<name>")
def user(name):
    return f"hey {name}!"
if __name__ == "__main__":
    app.run()
