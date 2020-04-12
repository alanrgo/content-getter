from controllers.v1.fetch_comment_controller import *
import sys

from controllers.v1.text_cleaner_controller import TextCleanerController

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    if len(sys.argv) == 1:
        print("\nPlease, insert the flag for the right scope:")
        print("--ytb: \tYoutube Tools\n")
        exit()

    if str(sys.argv[1]) == "--ytb":
        f_comment = FetchYoutubeCommentsController()
        f_comment.fetch_comment()

    if str(sys.argv[1] == "--txt"):
        text_controller = TextCleanerController()
        text_controller.remove_duplicate_lines()
