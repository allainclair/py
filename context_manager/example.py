class File:
    def __init__(self, filepath, mode='r'):
        self.filepath = filepath
        self.mode = mode

        self._file = None

    def __enter__(self):
        self._file = open(self.filepath, self.mode)
        return self

    def __exit__(self, exp_type, exp_value, exp_traceback):
        self._file.close()
        # return True  # Exceptions are handled and the file closed.

    def write(self, content):
        self._file.write(content)


def main():
    with File('example.txt', 'w') as file_:
        file_.write('First line\n')
        file_.write('Second line\n')


if __name__ == '__main__':
    main()
