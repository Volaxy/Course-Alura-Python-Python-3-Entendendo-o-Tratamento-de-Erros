class FileReader:
    def __init__(self, file):
        self.file = file
        raise FileNotFoundError
        print(f"Opening file: {self.file}")

    def read_next_line(self):
        raise IOError
        print("Reading line...")

        return "File line"

    def close(self):
        print("Closing file")


def __main__():
    reader = None
    try:
        reader = FileReader("test.txt")
        reader.read_next_line()
        reader.read_next_line()
        reader.read_next_line()
    except IOError:
        print("Exception of type IOError caught and treated")
    # The "finally" block will be executed regardless of whether there are errors or not
    finally:
        # The "locals()" verify all the local variables in this context
        if "reader" in locals():
            reader.close()


if __name__ == "__main__":
    __main__()
