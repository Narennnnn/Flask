# importing flask
from flask import Flask
from flask_restful  import Api,Resource


# create instance of Flask
app = Flask(__name__)
api=Api(app)
# route
class sayHey(Resource):
    def get(self):
        return {"title":"hey!"}
api.add_resource(sayHey,"/hey")
if __name__ == "__main__":
    app.run(debug=True)
