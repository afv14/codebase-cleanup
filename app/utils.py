
#moved from groceries file
def to_usd(my_price):
    """
    This function was designed to format numerical values
    to a U.S. currency, rounded to the nearest cent.

    This function accepts intergers, float, or complex data types.
    It will return a string data type.
    
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


   #"""
   #This is a docstring. It tells us what this function is about.
   #What its responsibilities are.
   #What the parameters are about.
   #What datatypes the parameters are.
   #What this function will return.
   #Example of invoking the function.

   #Invoke like this: to_usd(9.9999)

   #Example return value "$10,00"
   #"""