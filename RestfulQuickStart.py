from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)



class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Video(name={name}, views={views}, likes={likes})"

def test_connection(self):
    with app.app_context():
        db.create_all()

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video", required=True)
video_put_args.add_argument("likes", type=int, help="Likes of the video", required=True)

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer
}

class Video(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id):
        result = VideoModel.query.get(id=video_id)
        return jsonify(result), 200

    @marshal_with(resource_fields)
    def put(self, video_id):
        args = video_put_args.parse_args()
        video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
        db.session.add(video)
        db.session.commit()
        return jsonify(video), 201

api.add_resource(Video, "/video/<int:video_id>")


# @app.route("/")
# def home():
#     return "Home"
#
# @app.route("/get-user/<user_id>")
# def get_user(user_id):
#     user_data = {
#         "user_id": user_id,
#         "name": "John Doe",
#         "email": "john.doe@example.com"
#     }
#
#     extra = request.args.get("extra")
#     if extra:
#         user_data["extra"] = extra
#
#     return jsonify(user_data), 200
#
# @app.route("/create-user", methods=["POST"])
# def create_user():
#     data = request.get_json()
#
#     return jsonify(data), 201

if __name__ == "__main__":
    app.run(debug=True)

