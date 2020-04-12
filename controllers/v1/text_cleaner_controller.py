import argparse

from use_cases.text_cleaner_use_cases.remove_duplicate_lines import RemoveDuplicateLinesUseCase


class TextCleanerController:

    def __init__(self):
        return

    def remove_duplicate_lines(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--txt", help="invoke text formatting utils", action='store_true')
        parser.add_argument("--input", help="input file to be formatted")
        args = parser.parse_args()

        input_text = ""
        if args.input:
            f = open(args.input, "r")
            input_text = f.read()

        use_case = RemoveDuplicateLinesUseCase()
        output = use_case.remove_duplicate_lines(input_text)
        print(output)
