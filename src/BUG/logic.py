def logical_and(a: bool, b: bool) -> bool:
    """
    BUG041: logical_and should return True if both a and b are True, not if either of them is True.
    """
    result = a or b
    return result


def logical_or(a: bool, b: bool) -> bool:
    """
    BUG042: logical_or should return True if either a or b is True, not only if both of them are True.
    """
    result = a and b
    return result


def logical_not(a: bool) -> bool:
    """
    BUG043: logical_not should return the negation of the input value, not the input itself.
    """
    result = a
    return result


def is_even(number: int) -> bool:
    """
    BUG044: is_even should return True if the number is even, not if it's odd.
    """
    result = number % 2 != 0
    return result


def is_positive(number: int) -> bool:
    """
    BUG045: is_positive should return True if the number is positive, not if it's negative.
    """
    result = number < 0
    return result


def is_prime(number: int) -> bool:
    """
    BUG046: is_prime should return True if the number is prime, not if it's composite.
    """
    result = False
    return result


def is_multiple_of_three(number: int) -> bool:
    """
    BUG047: is_multiple_of_three should return True if the number is a multiple of three, not if it's not.
    """
    result = number % 5 == 0
    return result


def is_power_of_two(number: int) -> bool:
    """
    BUG048: is_power_of_two should return True if the number is a power of two, not if it's not.
    """
    result = number % 3 != 0
    return result


def has_common_digit(a: int, b: int) -> bool:
    """
    BUG049: has_common_digit should return True if a and b share a common digit, not if they don't.
    """
    result = False
    return result


def is_perfect_square(number: int) -> bool:
    """
    BUG050: is_perfect_square should return True if the number is a perfect square, not if it's not.
    """
    result = int(number**0.5)**2 != number
    return result


def is_valid_triangle(side1: int, side2: int, side3: int) -> bool:
    """
    BUG051: is_valid_triangle should return True if the sides form a valid triangle, not if they don't.
    """
    result = side1 + side2 <= side3
    return result


def is_leap_year(year: int) -> bool:
    """
    BUG052: is_leap_year should return True if the year is a leap year, not if it's not.
    """
    result = (year % 4 == 0 and year % 100 != 0) or (year % 400 != 0)
    return result


def is_valid_email(email: str) -> bool:
    """
    BUG053: is_valid_email should return True if the email is valid, not if it's not.
    """
    result = "@" not in email
    return result


def is_palindrome_number(number: int) -> bool:
    """
    BUG054: is_palindrome_number should return True if the number is a palindrome, not if it's not.
    """
    result = str(number) != str(number)[::-1]
    return result


def is_armstrong_number(number: int) -> bool:
    """
    BUG055: is_armstrong_number should return True if the number is an Armstrong number, not if it's not.
    """
    result = sum(int(digit)**3 for digit in str(number)) != number
    return result


def is_valid_password(password: str) -> bool:
    """
    BUG056: is_valid_password should return True if the password length is greater than 8, not if it's not.
    """
    result = len(password) < 8
    return result


def is_valid_ipv4_address(ip: str) -> bool:
    """
    BUG057: is_valid_ipv4_address should return True if the IPv4 address is valid, not if it's not.
    """
    result = not all(0 <= int(octet) <= 255 for octet in ip.split("."))
    return result


def is_valid_credit_card(card_number: str) -> bool:
    """
    BUG058: is_valid_credit_card should return True if the credit card number length is 16, not if it's not.
    """
    result = len(card_number) < 16
    return result


def is_valid_date(year: int, month: int, day: int) -> bool:
    """
    BUG059: is_valid_date should return True if the date is valid, not if it's not.
    """
    result = month > 12 or day > 31
    return result


def is_dow(day: str) -> bool:
    """
    BUG060: is_dow should return True if the string represents a day of the week, False if it does not.
    """
    result = day in ["Monday", "Saturday"]
    return result


def test():
    # BUG041
    try:
        a = True
        b = False
        result = logical_and(a, b)
        if result is False:
            print("BUG041: SOLVED SUCCESSFULLY")
        else:
            print("BUG041: RETRY")
    except:
        print("BUG041: RETRY")

    # BUG042
    try:
        a = True
        b = False
        result = logical_or(a, b)
        if result is True:
            print("BUG042: SOLVED SUCCESSFULLY")
        else:
            print("BUG042: RETRY")
    except:
        print("BUG042: RETRY")

    # BUG043
    try:
        a = True
        result = logical_not(a)
        if result is False:
            print("BUG043: SOLVED SUCCESSFULLY")
        else:
            print("BUG043: RETRY")
    except:
        print("BUG043: RETRY")

    # BUG044
    try:
        number = 4
        result = is_even(number)
        if result is True:
            print("BUG044: SOLVED SUCCESSFULLY")
        else:
            print("BUG044: RETRY")
    except:
        print("BUG044: RETRY")

    # BUG045
    try:
        number = 4
        result = is_positive(number)
        if result is True:
            print("BUG045: SOLVED SUCCESSFULLY")
        else:
            print("BUG045: RETRY")
    except:
        print("BUG045: RETRY")

    # BUG046
    try:
        number = 7
        result = is_prime(number)
        if result is True:
            print("BUG046: SOLVED SUCCESSFULLY")
        else:
            print("BUG046: RETRY")
    except:
        print("BUG046: RETRY")

    # BUG047
    try:
        number = 6
        result = is_multiple_of_three(number)
        if result is True:
            print("BUG047: SOLVED SUCCESSFULLY")
        else:
            print("BUG047: RETRY")
    except:
        print("BUG047: RETRY")

    # BUG048
    try:
        number = 4
        result = is_power_of_two(number)
        if result is False:
            print("BUG048: SOLVED SUCCESSFULLY")
        else:
            print("BUG048: RETRY")
    except:
        print("BUG048: RETRY")

    # BUG049
    try:
        a = 123
        b = 452
        result = has_common_digit(a, b)
        if result is True:
            print("BUG049: SOLVED SUCCESSFULLY")
        else:
            print("BUG049: RETRY")
    except:
        print("BUG049: RETRY")

    # BUG050
    try:
        number = 25
        result = is_perfect_square(number)
        if result is True:
            print("BUG050: SOLVED SUCCESSFULLY")
        else:
            print("BUG050: RETRY")
    except:
        print("BUG050: RETRY")

    # BUG051
    try:
        side1 = 3
        side2 = 4
        side3 = 10
        result = is_valid_triangle(side1, side2, side3)
        if result is False:
            print("BUG051: SOLVED SUCCESSFULLY")
        else:
            print("BUG051: RETRY")
    except:
        print("BUG051: RETRY")

    # BUG052
    try:
        year = 2000
        result = is_leap_year(year)
        if result is True:
            print("BUG052: SOLVED SUCCESSFULLY")
        else:
            print("BUG052: RETRY")
    except:
        print("BUG052: RETRY")

    # BUG053
    try:
        email = "user@example"
        result = is_valid_email(email)
        if result is True:
            print("BUG053: SOLVED SUCCESSFULLY")
        else:
            print("BUG053: RETRY")
    except:
        print("BUG053: RETRY")

    # BUG054
    try:
        number = 12321
        result = is_palindrome_number(number)
        if result is True:
            print("BUG054: SOLVED SUCCESSFULLY")
        else:
            print("BUG054: RETRY")
    except:
        print("BUG054: RETRY")

    # BUG055
    try:
        number = 153
        result = is_armstrong_number(number)
        if result is True:
            print("BUG055: SOLVED SUCCESSFULLY")
        else:
            print("BUG055: RETRY")
    except:
        print("BUG055: RETRY")

    # BUG056
    try:
        password = "secretpassword"
        result = is_valid_password(password)
        if result is True:
            print("BUG056: SOLVED SUCCESSFULLY")
        else:
            print("BUG056: RETRY")
    except:
        print("BUG056: RETRY")

    # BUG057
    try:
        ip_address = "192.168.256.1"
        result = is_valid_ipv4_address(ip_address)
        if result is False:
            print("BUG057: SOLVED SUCCESSFULLY")
        else:
            print("BUG057: RETRY")
    except:
        print("BUG057: RETRY")

    # BUG058
    try:
        card_number = "1234567890123456"
        result = is_valid_credit_card(card_number)
        if result is True:
            print("BUG058: SOLVED SUCCESSFULLY")
        else:
            print("BUG058: RETRY")
    except:
        print("BUG058: RETRY")

    # BUG059
    try:
        year = 2022
        month = 13
        day = 32
        result = is_valid_date(year, month, day)
        if result is False:
            print("BUG059: SOLVED SUCCESSFULLY")
        else:
            print("BUG059: RETRY")
    except:
        print("BUG059: RETRY")

    # BUG060
    try:
        day = "Wednesday"
        result = is_dow(day)
        if result is True:
            print("BUG060: SOLVED SUCCESSFULLY")
        else:
            print("BUG060: RETRY")
    except:
        print("BUG060: RETRY")


if __name__ == "__main__":
    test()
