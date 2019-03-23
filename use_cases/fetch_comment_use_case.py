from clients.youtube_comment_api_client import *

class Fetch_Youtube_Comment_Use_Case():

    def fetch_comment(self, args):
        print(args)
        api = YouTubeApi()
        api.get_video_comment(args)