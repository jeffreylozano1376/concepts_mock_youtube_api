from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

# determines if a request meets the requirement to either be allowed or denied
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True) # requirement 1
video_put_args.add_argument("views", type=int, help="Views of the video", required=True) # requirement 2
video_put_args.add_argument("likes", type=int, help="Likes on the video", required=True) # requirement 3

videos = {}

# sends back an error message if 'video doesnt exist'
def abort_if_video_id_doesnt_exist(video_id):
    if video_id not in videos:
        abort(404, message="Could not find video...")

# sends back an error message if 'video exists'
def abort_if_video_exists(video_id):
    if video_id in videos:
        abort(409, message="Video already exist with that ID...")

# Create Resource
class Video(Resource):
    # returns info according to requested video_id
    def get(self, video_id):
        abort_if_video_id_doesnt_exist(video_id)
        return videos[video_id]
    # create new video
    def put(self, video_id):
        abort_if_video_exists(video_id)
        args = video_put_args.parse_args() # parses the requirements
        videos[video_id] = args
        return videos[video_id], 201 # video successfully created
    # delete video
    def delete(self, video_id):
        abort_if_video_id_doesnt_exist(video_id)
        del videos[video_id]
        return '', 204 # video successfully deleted

# Register Resource (Class, "API Endpoint/<parameter>")
api.add_resource(Video, "/video/<int:video_id>")

if __name__=="__main__":
    app.run(debug=True)