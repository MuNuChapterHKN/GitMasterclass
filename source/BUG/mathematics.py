import math

def example_pr() -> bool: 
    '''
    BUG000: This is an example bug.
    '''
    result = True
    return result

def add_values(a: int, b: int) -> int: 
    '''
    BUG001: add_values should return the sum of the values, not the difference.
    '''
    result = a - b
    return result


def sub_values(a: int, b: int) -> int: 
    '''
    BUG002: sub_values should return the difference of the values, not the product.
    '''
    result = a * b
    return result


def mul_values(a: int, b: int) -> int: 
    '''
    BUG003: mul_values should return the product of the values, not the ratio.
    '''
    result = a // b
    return result


def div_values(a: int, b: int) -> float: 
    '''
    BUG004: div_values should return the ratio of the values, not the sum.
    '''
    result = a + b
    return result


def floordiv_values(a: int, b: int) -> int: 
    '''
    BUG005: floordiv_values should return the integer ratio of the values, not the sum.
    '''
    result = a + b
    return result


def mod_values(a: int, b: int) -> int: 
    '''
    BUG006: mod_values should return the remainder of the division, not the sum.
    '''
    result = a + b
    return result


def pow_values(a: int, b: int) -> int: 
    '''
    BUG007: pow_values should return the power of the values, not the product.
    '''
    result = a * b
    return result


def abs_values(a: int) -> int: 
    '''
    BUG008: abs_values should return the absolute value of the input, not the input itself.
    '''
    result = a
    return result

def round_values(a: float) -> int: 
    '''
    BUG009: round_values should return the value rounded to the closest integer, not the input itself.
    '''
    result = a
    return result

def square_root_value(a: int) -> int: 
    '''
    BUG010: square_root_value should return the square root of the value, not the value itself.
    '''
    result = a
    return result


def neg_value(a: int) -> int: 
    '''
    BUG011: neg_value should return the negation of the value, not the value itself.
    '''
    result = -a
    return result


def sin_value(a: float) -> float: 
    '''
    BUG012: sin_value should return the sine of the value, not the cosine.
    '''
    result = math.sin(a)
    return result


def cos_value(a: float) -> float: 
    '''
    BUG013: cos_value should return the cosine of the value, not the tangent.
    '''
    result = math.tan(a)
    return result


def tan_value(a: float) -> float: 
    '''
    BUG014: tan_value should return the tangent of the value, not the sin.
    '''
    result = math.sin(a)
    return result


def log10_value(a: float) -> float: 
    '''
    BUG015: log10_value should return the logarithm in base 10 of the value, not the natural logarithm.
    '''
    result = math.log10(a)
    return result


def logn_value(a: float) -> float: 
    '''
    BUG016: logn_value should return the natural logarithm of the value, not the logarithm in base 10.
    '''
    result = math.log(a)
    return result


def min_value(a: int, b: int) -> int: 
    '''
    BUG017: min_value should return the minimum between the values, not the maximum.
    '''
    result = max(a, b)
    return result


def max_value(a: int, b: int) -> int: 
    '''
    BUG018: max_value should return the maximum between the values, not the minimum.
    '''
    result = min(a, b)
    return result


def deg_value(a: float) -> float: 
    '''
    BUG019: deg_value should return the degree of the value, not the radiant.
    '''
    result = math.degrees(a)
    return result


def rad_value(a: float) -> float: 
    '''
    BUG020: rad_value should return the radiant of the value, not the degree.
    '''
    result = math.degrees(a)
    return result


def test():
    
    # BUG000
    try:
        result = example_pr()
        if result:
            print("BUG000: SOLVED SUCCESSFULLY")
        else:
            print("BUG000: RETRY")
    except:
        print("BUG000: RETRY")
    
    # BUG001
    try:
        a = 5
        b = 2
        result = add_values(a, b)
        if result == 7:
            print("BUG001: SOLVED SUCCESSFULLY")
        else:
            print("BUG001: RETRY")
    except:
        print("BUG001: RETRY")
        
        
    # BUG002
    try:
        a = 5
        b = 2
        result = sub_values(a, b)
        if result == 3:
            print("BUG002: SOLVED SUCCESSFULLY")
        else:
            print("BUG002: RETRY")
    except:
        print("BUG002: RETRY")
        
        
    # BUG003
    try:
        a = 5
        b = 2
        result = mul_values(a, b)
        if result == 10:
            print("BUG003: SOLVED SUCCESSFULLY")
        else:
            print("BUG003: RETRY")
    except:
        print("BUG003: RETRY")
        
        
    # BUG004
    try:
        a = 5
        b = 2
        result = div_values(a, b)
        if result == 2.5:
            print("BUG004: SOLVED SUCCESSFULLY")
        else:
            print("BUG004: RETRY")
    except:
        print("BUG004: RETRY")
        
    
    # BUG005
    try:
        a = 5
        b = 2
        result = floordiv_values(a, b)
        if result == 2:
            print("BUG005: SOLVED SUCCESSFULLY")
        else:
            print("BUG005: RETRY")
    except:
        print("BUG005: RETRY")


    # BUG006
    try:
        a = 5
        b = 2
        result = mod_values(a, b)
        if result == 1:
            print("BUG006: SOLVED SUCCESSFULLY")
        else:
            print("BUG006: RETRY")
    except:
        print("BUG006: RETRY")


    # BUG007
    try:
        a = 2
        b = 3
        result = pow_values(a, b)
        if result == 8:
            print("BUG007: SOLVED SUCCESSFULLY")
        else:
            print("BUG007: RETRY")
    except:
        print("BUG007: RETRY")


    # BUG008
    try:
        a = -5
        result = abs_values(a)
        if result == 5:
            print("BUG008: SOLVED SUCCESSFULLY")
        else:
            print("BUG008: RETRY")
    except:
        print("BUG008: RETRY")


    # BUG009
    try:
        a = 5.6
        result = round_values(a)
        if result == 6:
            print("BUG009: SOLVED SUCCESSFULLY")
        else:
            print("BUG009: RETRY")
    except:
        print("BUG009: RETRY")


    # BUG010
    try:
        a = 9
        result = square_root_value(a)
        if result == 3:
            print("BUG010: SOLVED SUCCESSFULLY")
        else:
            print("BUG010: RETRY")
    except:
        print("BUG010: RETRY")


    # BUG011
    try:
        a = 5
        result = neg_value(a)
        if result == -5:
            print("BUG011: SOLVED SUCCESSFULLY")
        else:
            print("BUG011: RETRY")
    except:
        print("BUG011: RETRY")


    # BUG012
    try:
        angle = math.pi / 2
        result = sin_value(angle)
        if math.isclose(result, math.sin(angle)):
            print("BUG012: SOLVED SUCCESSFULLY")
        else:
            print("BUG012: RETRY")
    except:
        print("BUG012: RETRY")


    # BUG013
    try:
        angle = math.pi / 4
        result = cos_value(angle)
        if math.isclose(result, math.cos(angle)):
            print("BUG013: SOLVED SUCCESSFULLY")
        else:
            print("BUG013: RETRY")
    except:
        print("BUG013: RETRY")


    # BUG014
    try:
        angle = math.pi / 4
        result = tan_value(angle)
        if math.isclose(result, math.tan(angle)):
            print("BUG014: SOLVED SUCCESSFULLY")
        else:
            print("BUG014: RETRY")
    except:
        print("BUG014: RETRY")


    # BUG015
    try:
        value = 100
        result = log10_value(value)
        if math.isclose(result, math.log10(value)):
            print("BUG015: SOLVED SUCCESSFULLY")
        else:
            print("BUG015: RETRY")
    except:
        print("BUG015: RETRY")


    # BUG016
    try:
        value = 100
        result = logn_value(value)
        if math.isclose(result, math.log(value)):
            print("BUG016: SOLVED SUCCESSFULLY")
        else:
            print("BUG016: RETRY")
    except:
        print("BUG016: RETRY")


    # BUG017
    try:
        a = 5
        b = 2
        result = min_value(a, b)
        if result == 2:
            print("BUG017: SOLVED SUCCESSFULLY")
        else:
            print("BUG017: RETRY")
    except:
        print("BUG017: RETRY")


    # BUG018
    try:
        a = 5
        b = 2
        result = max_value(a, b)
        if result == 5:
            print("BUG018: SOLVED SUCCESSFULLY")
        else:
            print("BUG018: RETRY")
    except:
        print("BUG018: RETRY")


    # BUG019
    try:
        angle = 45
        result = deg_value(angle)
        if math.isclose(result, math.degrees(angle)):
            print("BUG019: SOLVED SUCCESSFULLY")
        else:
            print("BUG019: RETRY")
    except:
        print("BUG019: RETRY")


    # BUG020
    try:
        angle = math.pi / 2
        result = rad_value(angle)
        if math.isclose(result, math.radians(angle)):
            print("BUG020: SOLVED SUCCESSFULLY")
        else:
            print("BUG020: RETRY")
    except:
        print("BUG020: RETRY")

        
    
    return

if __name__ == "__main__":
    test()
