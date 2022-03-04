from division import divide, test_division


def __main__():
    # When an error is executed, the Python will show what file the error is occurred, the line of the error, and the
    # type of this error, followed by the description
    # print("Hello, World!"))

    # phrase = "Hello, World!"
    # The error below is an exception, which is different from an error
    # print(phrase.hello)

    # The traceback is read from bottom to top, and it is divided as follows (from bottom to top):
    # The Type Error ou the Attribute Error, followed by the description
    # The origin of the Error, followed by the number line, and the file where the error is occurred
    # The call stack from methods
    test_division(0)


if __name__ == "__main__":
    __main__()
