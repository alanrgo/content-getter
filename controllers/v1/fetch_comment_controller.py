import argparse
from use_cases.fetch_comment_use_case import * 

class Fetch_Youtube_Comments_Controller():

    def fetch_comment(self):
        parser = argparse.ArgumentParser()
        mxRes = 20
        vid = str()
        parser.add_argument("--ytb", help="calls comment function by keyword function", action='store_true')
        parser.add_argument("--c", help="calls comment function by keyword function", action='store_true')
        parser.add_argument("--max", help="number of comments to return")
        parser.add_argument("--videourl", help="Required URL for which comments to return")
        parser.add_argument("--key", help="Required API key")

        args = parser.parse_args()

        if not args.max:
            args.max = mxRes

        if not args.videourl:
            exit("Please specify video URL using the --videourl=parameter.")

        if not args.key:
            exit("Please specify API key using the --key=parameter.")
            
        use_case = Fetch_Youtube_Comment_Use_Case()
        use_case.fetch_comment(args)