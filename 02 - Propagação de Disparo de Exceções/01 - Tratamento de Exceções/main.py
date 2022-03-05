from division import divide, test_division


def __main__():
    try:
        test_division(0)
    # The "as" define a variable represented by the exception
    except ZeroDivisionError as e:
        print("The exception ZeroDivisionError is occurred and was treated")
        print(e)
        print(e.__class__.__bases__)
    # The "Exception" is the parent of all exceptions, the treat of this exception is the polymorphism
    # The order of the treatment of the errors, is defined by treat the less generic at the most generic, allowing the
    # most specific exceptions to be handled first
    # except Exception as e:
    #    print(e)


if __name__ == "__main__":
    __main__()
