# Import necessary modules
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

# Create Flask app
app = Flask(__name__)
api = Api(app)

# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# Define VideoModel class
class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

# Define fields for serialization
video_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer
}

# Request parser for video data
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video", required=True)
video_put_args.add_argument("likes", type=int, help="Likes on the video", required=True)

video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="Name of the video")
video_update_args.add_argument("views", type=int, help="Views of the video")
video_update_args.add_argument("likes", type=int, help="Likes on the video")

# Resource class for handling video operations
class Video(Resource):
    @marshal_with(video_fields)
    def get(self, video_id):
        video = VideoModel.query.filter_by(id=video_id).first()
        if not video:
            abort(404, message="Video not found")
        return video

    @marshal_with(video_fields)
    def put(self, video_id):
        args = video_put_args.parse_args()
        video = VideoModel.query.filter_by(id=video_id).first()
        if video:
            abort(409, message="Video already exists")
        video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
        db.session.add(video)
        db.session.commit()
        return video, 201

    @marshal_with(video_fields)
    def patch(self, video_id):
        args = video_update_args.parse_args()
        video = VideoModel.query.filter_by(id=video_id).first()
        if not video:
            abort(404, message="Video not found")
        if args['name']:
            video.name = args['name']
        if args['views']:
            video.views = args['views']
        if args['likes']:
            video.likes = args['likes']
        db.session.commit()
        return video

    def delete(self, video_id):
        video = VideoModel.query.filter_by(id=video_id).first()
        if not video:
            abort(404, message="Video not found")
        db.session.delete(video)
        db.session.commit()
        return '', 204

# Add the resource to the API with route "/video/<int:video_id>"
api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)
