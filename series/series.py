def fibonacci(n):
    """Fibonacci Function

    Args:
        n 
    
    This function adds the previous numbers from the base numbers of 0,1 adding the numbers before it together until the nth number in the series.
    """
    if n<0:
        return ("Negative numbers are not supported")
    if n==0:
        return 0
    if n==1:
        return 1
    elif n>1:
        return (fibonacci(n-1)+fibonacci(n-2))
    else:
        return ("Inconceivable!")

def lucas(n):
    """Lucas Function

    Args:
        n 
    
    This function adds the previous numbers from the base numbers of 2,1 adding the numbers before it together until the nth number in the series.
    """
    if n<0:
        return ("Negative numbers are not supported")
    if n==0:
        return 2
    if n==1:
        return 1
    elif n>1:
        return (lucas(n-1)+lucas(n-2))
    else:
        return ("Inconceivable!")