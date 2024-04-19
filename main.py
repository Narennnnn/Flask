# importing flask
from flask import Flask
from flask_restful  import Api,Resource,reqparse,abort


# create instance of Flask
app = Flask(__name__)
api=Api(app)

video_put_args= reqparse.RequestParser()
video_put_args.add_argument("name",type=str,help="Name of the video")
video_put_args.add_argument("views",type=str,help="Views of the video")
video_put_args.add_argument("likes",type=str,help="Likes on the video")
videos={}

def abortIfNotId(video_id):
    if video_id not in videos:
        abort(404,messae="Incorrect Id request")

class video(Resource):
    def get(self,video_id):
        abortIfNotId(video_id)
        return videos[video_id]
    def put(self,video_id):
        args=video_put_args.parse_args()
        videos[video_id]=args
        return videos[video_id],201
api.add_resource(video,"/video/<int:video_id>")
if __name__ == "__main__":
    app.run(debug=True)
