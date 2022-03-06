class FileReader:
    def __init__(self, file):
        self.file = file
        print(f"Opening file: {self.file}")

    def read_next_line(self):
        print("Reading line...")

        return "File line"

    def close(self):
        print("Closing file")

    # When passing through "with", it calls this method
    def __enter__(self):
        return self

    # On the output of "with", it calls this method, releasing the resources
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing file")


def __main__():
    # The "with" open and close the resource at the beginning of the code block, and the end respectively
    with FileReader("test.txt") as reader:
        reader.read_next_line()
        reader.read_next_line()
        reader.read_next_line()


if __name__ == "__main__":
    __main__()
