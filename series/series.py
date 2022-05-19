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

def sum_series(n, a=0, b=1):
    # Setting a value for a and b here makes it so the user does not have to set a value aka they are optional.
    if (a==0 and b==1):
        return fibonacci(n)
    elif (a==2 and b==1):
        return lucas(n)
    elif a<0 or b<0 or n<0:
        return ("Negative numbers are not supported")
    elif (a>0 and b>=0) or (b>0 and a>=0) or (b>0 and a>0) and n>0:
        if n==0:
             return a
        elif n==1:
            return b
        elif n>1:
            return (sum_series(n-1, a, b)+sum_series(n-2, a, b))

print (sum_series(5,3,4))

# print (sum_series(5,3,4))
#3,4,7,11,18,29