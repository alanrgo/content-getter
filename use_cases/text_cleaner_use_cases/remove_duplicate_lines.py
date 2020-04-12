
class RemoveDuplicateLinesUseCase:

    def __init__(self):
        return

    def remove_duplicate_lines(self, text):
        lines = text.split('\n')
        if len(lines) == 1:
            return lines[0]

        output = ""
        for i in range(1, len(lines)):
            previous_line = i-1
            if lines[previous_line] != lines[i]:
                output = output + lines[previous_line] + '\n'

        last_line = len(lines) - 1
        output = output + lines[last_line]
        return output
