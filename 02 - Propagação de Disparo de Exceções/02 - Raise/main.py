from division import test_division


def __main__():
    try:
        test_division(2.5)
    except ZeroDivisionError as e:
        print("The exception ZeroDivisionError is occurred and was treated")
        print(e)
        print(e.__class__.__bases__)


if __name__ == "__main__":
    __main__()
