def divide(dividend, divider):
    return dividend / divider


def test_division(divider):
    # The "try" involves the code which as error sensitive
    try:
        divider.helo
        result = divide(10, divider)
        print(f"The result of the division of 10 by {divider} is {result}")
    # The "except" handles the error if it happens in the try block

    # The program running without any problem, doesn't mean that he is executed correctly, but that ran the program
    # without stopping abruptly

    # To treat an exception, just put the Exception Name after the "except", followed by the code which will be executed
    # when the exception occurs

    # When an exception occurs, it checks if the current scope has a treatment for it, if not, the method call is made
    # from the most nested to the least nested until it finds someone who handles the exception, making it impossible
    # for other exceptions to be thrown if the exception occurs. their code block cannot handle certain exceptions
    except ZeroDivisionError:
        print("The exception ZeroDivisionError is occurred and was treated")
    except AttributeError:
        print("The exception AttributeError is occurred and was treated")
