def divide(dividend, divider):
    return dividend / divider


def test_division(divider):
    result = divide(10, divider)

    print(f"The result of the division of 10 by {divider} is {result}")
