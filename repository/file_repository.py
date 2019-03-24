class FileRepository:

    WRITE_AND_OR_CREATE_FILE = "w+"

    def open_file(self, file_name):
        f = open(file_name, self.WRITE_AND_OR_CREATE_FILE)
        return f

    def write_string_in_file(self, file, string):
        file.write(string)
        file.write("\n")
    
    def close_file(self, file):
        file.close()