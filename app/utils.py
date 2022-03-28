
#moved from groceries file
def to_usd(my_price):
    """
    This is a docstring. It tells us what this function is about.
    What its responsibilities are.
    What the parameters are about.
    What datatypes the parameters are.
    What this function will return.
    Example of invoking the function.

    Invoke like this: to_usd(9.9999)
    """
    return '${:,.2f}'.format(my_price)