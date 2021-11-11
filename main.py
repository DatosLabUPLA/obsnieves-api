from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

names = {
    "tim": {"age": 19, "gender": "male"},
    "bill": {"age": 77, "gender": "female"},
    }

class HelloWorld(Resource):
    def get(self, name):
        return names[name]

    # def post(self):
    #     return {"data": "Hello World"}

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, required=True, help="Name cannot be blank")
video_put_args.add_argument("views", type=int, required=True, help="Views cannot be blank")
video_put_args.add_argument("likes", type=int, required=True, help="Likes cannot be blank")

videos = {}

class Video(Resource):
    def get(self, video_id):
        return videos[videos_id]

    def put(self, video_id):
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201

api.add_resource(HelloWorld, '/helloworld/<string:name>')
api.add_resource(Video, '/videos/<int:video_id>')

if __name__ == '__main__':
    app.run(debug=True)


