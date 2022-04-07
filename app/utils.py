
#moved from groceries file
def to_usd(my_price):
    """
    This function was designed to format values to
    a U.S. currency, rounded to two decimal places.
    
    Example of invoking the function.

    Invoke like this: to_usd(9.9999)

    Example return value "$10,00"
    """
    return '${:,.2f}'.format(my_price)


if __name__ == "__main__":

    #if this code is in the global scope of a file we are trying to import from
    #it will throw errors when we try to run those
    #have to nest this code in the main conditional

    #nesting code in the main condition will allow other scripts to cleanly
    #import without running this code

    #this code still gets run when we invoke the script from the command line

    price = input ('Please choose a price like 4.9999')

    print (to_usd(float(price)))


