from clients.youtube_comment_api_client import YouTubeApi
from repository.file_repository import *

class Fetch_Youtube_Comment_Use_Case:

    def __init__(self, file_repository = FileRepository()):
        self.file_repository = file_repository

    def fetch_comment(self, args):
        api = YouTubeApi()
        comment_data = api.get_video_comment(args)
        f = self.file_repository.open_file("dummy_name.csv")
        for comment in comment_data:
            line = ";".join(comment)
            line.replace("\r\n", " $ ")
            self.file_repository.write_string_in_file(f, line)

