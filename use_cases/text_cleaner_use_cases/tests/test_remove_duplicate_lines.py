import unittest

from use_cases.text_cleaner_use_cases.remove_duplicate_lines import RemoveDuplicateLinesUseCase


class TestRemoveDuplicateLines(unittest.TestCase):

    def test_empty_string(self):
        expected = ''
        use_case = RemoveDuplicateLinesUseCase()
        received = use_case.remove_duplicate_lines('')

        self.assertEquals(received, expected)

    def test_duplicated_lines(self):
        input_text = 'Hello World\nHello World\n'
        use_case = RemoveDuplicateLinesUseCase()
        received = use_case.remove_duplicate_lines(input_text)
        expected = 'Hello World\n'

        self.assertEquals(received, expected)

    def test_not_duplicated_lines(self):
        input_text = 'Hello World 1\nHello World 2\n'
        use_case = RemoveDuplicateLinesUseCase()
        received = use_case.remove_duplicate_lines(input_text)
        expected = input_text

        self.assertEquals(received, expected)

    def test_duplicated_lines_in_a_bigger_text(self):
        input_text = 'Hello World 1\n' \
                     'Hello World 2\n' \
                     'Hello World 2\n' \
                     'Hello World 3\n'
        use_case = RemoveDuplicateLinesUseCase()
        received = use_case.remove_duplicate_lines(input_text)
        expected = 'Hello World 1\n' \
                   'Hello World 2\n' \
                   'Hello World 3\n'

        self.assertEquals(received, expected)

    def test_duplicated_lines_in_last_two_lines(self):
        input_text = 'Hello World 1\n' \
                     'Hello World 2\n' \
                     'Hello World 3\n' \
                     'Hello World 3\n'
        use_case = RemoveDuplicateLinesUseCase()
        received = use_case.remove_duplicate_lines(input_text)
        expected = 'Hello World 1\n' \
                   'Hello World 2\n' \
                   'Hello World 3\n'

        self.assertEquals(received, expected)
