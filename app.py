from controllers.v1.fetch_comment_controller import *
import sys

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    if str(sys.argv[1]) == "--ytb":
        f_comment = Fetch_Youtube_Comments_Controller()
        f_comment.fetch_comment()
