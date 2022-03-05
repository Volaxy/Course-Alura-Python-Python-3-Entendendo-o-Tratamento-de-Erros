def divide(dividend, divider):
    # The "isinstance()" verify the type of the variable matches with the second parameter in the function
    if not (isinstance(dividend, int) and isinstance(divider, int)):
        # This "raise" propagates the exception type describes after the "raise", with a description of the error
        raise ValueError("divide() must receive only integer arguments")

    try:
        return dividend / divider
        # If the return is not executed, the return default value is "None"
    except:
        print(f"Could not divide {dividend} by {divider}")
        # The "raise" takes the context of the exception, and propagates it to the program
        raise


def test_division(divider):
    result = divide(10, divider)
    print(f"The result of the division of 10 by {divider} is {result}")
