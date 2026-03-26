class FileManager:
    def read_entire_file(self, path, mode):
        with open(path, mode) as reader:
            print(reader.read())

    def get_file_lines(self, path, mode):
        with open(path, mode) as reader:
            return reader.readlines()

    def read_line_by_line(self, path, mode):
        with open(path, mode) as reader:
            line = reader.readline()
            while line != '':  
                print(line, end='')
                line = reader.readline()

    def write_text(self, path, text):
        with open(path, 'w') as file:
            file.write(text)