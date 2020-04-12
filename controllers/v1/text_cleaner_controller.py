from use_cases.text_cleaner_use_cases.remove_duplicate_lines import RemoveDuplicateLinesUseCase


class TextCleanerController:

    def __init__(self):
        return

    def remove_duplicate_lines(self):
        use_case = RemoveDuplicateLinesUseCase()
        use_case.remove_duplicate_lines("")
