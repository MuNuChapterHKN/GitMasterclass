def stalin_sort(array):
    '''
    BUG081
    '''
    # https://github.com/gustavo-depaula/stalin-sort

    
    return array


def inverse_factorial_sum(n: int) -> float:
    '''
    BUG082
    '''

    # https://www.youmath.it/forum/analisi-1/58596-serie-di-1n.html
    # Example:
    #           result = [1/(1!)] + [1/(2!)] + [1/(3!)] + ... + [1/(n!)]
    #                  
    
    return 0


def list_divisor(n: int) -> list:
    '''
    BUG083
    '''
    # Given an integer value `n`, return the list of its divisors 
    # sorted increasingly.
    
    return []


def gcd(a: int, b: int) -> int:
    '''
    BUG084
    '''
    # Implement the Great Common Divisor algorithm. 
    
    return 0


def lcm(a: int, b: int) -> int:
    '''
    BUG084
    '''
    # Implement the Least Common Multiple algorithm. 
    
    return 0

def test():
    
    # BUG081
    try:
        array = [1, 6, 5, 7, 2, 4, 9]
        if stalin_sort(array) == [1, 6, 7, 9]:
            print("BUG081: SOLVED SUCCESSFULLY")
        else:
            print("BUG081: RETRY")
    except:
        print("BUG081: RETRY")

    # BUG082
    try:
        n = 5
        result = inverse_factorial_sum(n)
        if result > 1.71 and result < 1.72:
            print("BUG082: SOLVED SUCCESSFULLY")
        else:
            print("BUG082: RETRY")
    except:
        print("BUG082: RETRY")

    # BUG083
    try:
        n = 120
        result = list_divisor(n)
        if result == [1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 24, 30, 40, 60, 120]:
            print("BUG083: SOLVED SUCCESSFULLY")
        else:
            print("BUG083: RETRY")
    except:
        print("BUG083: RETRY")

    # BUG044
    try:
        a = 252
        b = 378
        result = gcd(a, b)
        if result == 126:
            print("BUG084: SOLVED SUCCESSFULLY")
        else:
            print("BUG084: RETRY")
    except:
        print("BUG084: RETRY")

    # BUG045
    try:
        a = 452
        b = 23
        result = lcm(a, b)
        if result == 10396:
            print("BUG085: SOLVED SUCCESSFULLY")
        else:
            print("BUG085: RETRY")
    except:
        print("BUG085: RETRY")

    


if __name__ == "__main__":
    test()
