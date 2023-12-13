def concat_strings(str1: str, str2: str) -> str:
    """
    BUG021: concat_strings should concatenate two strings, not subtract them.
    """
    result = str1 - str2
    return result


def repeat_string(s: str, n: int) -> str:
    """
    BUG022: repeat_string should repeat the given string n times, not multiply its length.
    """
    result = s * len(s)
    return result


def capitalize_string(s: str) -> str:
    """
    BUG023: capitalize_string should capitalize the first letter of the string, not the entire string.
    """
    result = s.upper()
    return result


def lowercase_string(s: str) -> str:
    """
    BUG024: lowercase_string should convert the entire string to lowercase, not capitalize it.
    """
    result = s.capitalize()
    return result


def count_chars(s: str, char: str) -> int:
    """
    BUG025: count_chars should count the occurrences of a specific character in the string, not the total length.
    """
    result = len(s)
    return result


def index_of_substring(s: str, sub: str) -> int:
    """
    BUG026: index_of_substring should return the index of the first occurrence of a substring, not the entire string.
    """
    result = s
    return result


def replace_substring(s: str, old_sub: str, new_sub: str) -> str:
    """
    BUG027: replace_substring should replace occurrences of old_sub with new_sub, not append new_sub.
    """
    result = s + new_sub
    return result


def remove_whitespace(s: str) -> str:
    """
    BUG028: remove_whitespace should remove all whitespace from the string, not just leading and trailing whitespace.
    """
    result = s.strip()
    return result


def is_palindrome(s: str) -> bool:
    """
    BUG029: is_palindrome should check if the string is a palindrome.
    """
    result = False
    return result


def extract_digits(s: str) -> str:
    """
    BUG030: extract_digits should return a string containing only the digits from the input string, not convert it to int.
    """
    result = int(s)
    return result


def reverse_string(s: str) -> str:
    """
    BUG031: reverse_string should reverse the characters in the string, not concatenate the reversed string.
    """
    result = s + s[::-1]
    return result


def split_string(s: str, delimiter: str) -> list:
    """
    BUG032: split_string should split the string into a list of substrings using the given delimiter, not join them.
    """
    result = "".join(s.split(delimiter))
    return result


def count_vowels(s: str) -> int:
    """
    BUG033: count_vowels should count the number of vowels in the string, not the total length.
    """
    result = len(s)
    return result


def substring_before(s: str, sub: str) -> str:
    """
    BUG034: substring_before should return the substring before the first occurrence of sub, not after it.
    """
    result = s.split(sub)[1]
    return result


def substring_after(s: str, sub: str) -> str:
    """
    BUG035: substring_after should return the substring after the first occurrence of sub, not before it.
    """
    result = s.split(sub)[1]
    return result


def strip_non_alphanumeric(s: str) -> str:
    """
    BUG036: strip_non_alphanumeric should remove all non-alphanumeric characters, not just leading and trailing ones.
    """
    result = s.strip()
    return result


def is_alpha(s: str) -> bool:
    """
    BUG037: is_alpha should check if all characters in the string are alphabetic, not if the entire string is alphabetic.
    """
    result = s.isnumeric()
    return result


def is_numeric(s: str) -> bool:
    """
    BUG038: is_numeric should check if all characters in the string are numeric, not if the entire string is numeric.
    """
    result = s.isalpha() 
    return result


def join_strings(lst: list, delimiter: str) -> str:
    """
    BUG039: join_strings should join a list of strings using the given delimiter, not concatenate them.
    """
    result = "".join(lst)
    return result


def title_case(s: str) -> str:
    """
    BUG040: title_case should capitalize the first letter of each word, not the entire string.
    """
    result = s.upper()
    return result


def test():
    
    # BUG021
    try:
        str1 = "Hello"
        str2 = "World"
        result = concat_strings(str1, str2)
        if result == "HelloWorld":
            print("BUG021: SOLVED SUCCESSFULLY")
        else:
            print("BUG021: RETRY")
    except:
        print("BUG021: RETRY")

    # BUG022
    try:
        s = "abc"
        n = 2
        result = repeat_string(s, n)
        if result == "abcabc":
            print("BUG022: SOLVED SUCCESSFULLY")
        else:
            print("BUG022: RETRY")
    except:
        print("BUG022: RETRY")

    # BUG023
    try:
        s = "hello"
        result = capitalize_string(s)
        if result == "Hello":
            print("BUG023: SOLVED SUCCESSFULLY")
        else:
            print("BUG023: RETRY")
    except:
        print("BUG023: RETRY")

    # BUG024
    try:
        s = "Hello"
        result = lowercase_string(s)
        if result == "hello":
            print("BUG024: SOLVED SUCCESSFULLY")
        else:
            print("BUG024: RETRY")
    except:
        print("BUG024: RETRY")

    # BUG025
    try:
        s = "hello"
        char = "l"
        result = count_chars(s, char)
        if result == 2:
            print("BUG025: SOLVED SUCCESSFULLY")
        else:
            print("BUG025: RETRY")
    except:
        print("BUG025: RETRY")

    # BUG026
    try:
        s = "hello world"
        sub = "world"
        result = index_of_substring(s, sub)
        if result == 6:
            print("BUG026: SOLVED SUCCESSFULLY")
        else:
            print("BUG026: RETRY")
    except:
        print("BUG026: RETRY")

    # BUG027
    try:
        s = "Poodle"
        old_sub = "oo"
        new_sub = "ee"
        result = replace_substring(s, old_sub, new_sub)
        if result == "Peedle":
            print("BUG027: SOLVED SUCCESSFULLY")
        else:
            print("BUG027: RETRY")
    except:
        print("BUG027: RETRY")

    # BUG028
    try:
        s = "  hello world  "
        result = remove_whitespace(s)
        if result == "helloworld":
            print("BUG028: SOLVED SUCCESSFULLY")
        else:
            print("BUG028: RETRY")
    except:
        print("BUG028: RETRY")

    # BUG029
    try:
        s = "level"
        result = is_palindrome(s)
        if result:
            print("BUG029: SOLVED SUCCESSFULLY")
        else:
            print("BUG029: RETRY")
    except:
        print("BUG029: RETRY")

    # BUG030
    try:
        s = "12a34a5"
        result = extract_digits(s)
        if result == "12345":
            print("BUG030: SOLVED SUCCESSFULLY")
        else:
            print("BUG030: RETRY")
    except:
        print("BUG030: RETRY")

    # BUG031
    try:
        s = "hello"
        result = reverse_string(s)
        if result == "olleh":
            print("BUG031: SOLVED SUCCESSFULLY")
        else:
            print("BUG031: RETRY")
    except:
        print("BUG031: RETRY")

    # BUG032
    try:
        s = "hello world"
        delimiter = " "
        result = split_string(s, delimiter)
        if result == ["hello", "world"]:
            print("BUG032: SOLVED SUCCESSFULLY")
        else:
            print("BUG032: RETRY")
    except:
        print("BUG032: RETRY")

    # BUG033
    try:
        s = "hello"
        result = count_vowels(s)
        if result == 2:
            print("BUG033: SOLVED SUCCESSFULLY")
        else:
            print("BUG033: RETRY")
    except:
        print("BUG033: RETRY")

    # BUG034
    try:
        s = "hello world"
        sub = "world"
        result = substring_before(s, sub)
        if result == "hello ":
            print("BUG034: SOLVED SUCCESSFULLY")
        else:
            print("BUG034: RETRY")
    except:
        print("BUG034: RETRY")

    # BUG035
    try:
        s = "hello world"
        sub = "hello"
        result = substring_after(s, sub)
        if result == " world":
            print("BUG035: SOLVED SUCCESSFULLY")
        else:
            print("BUG035: RETRY")
    except:
        print("BUG035: RETRY")

    # BUG036
    try:
        s = "  hello world  !"
        result = strip_non_alphanumeric(s)
        if result == "helloworld":
            print("BUG036: SOLVED SUCCESSFULLY")
        else:
            print("BUG036: RETRY")
    except:
        print("BUG036: RETRY")

    # BUG037
    try:
        s = "hello"
        result = is_alpha(s)
        if result:
            print("BUG037: SOLVED SUCCESSFULLY")
        else:
            print("BUG037: RETRY")
    except:
        print("BUG037: RETRY")

    # BUG038
    try:
        s = "12345"
        result = is_numeric(s)
        if result:
            print("BUG038: SOLVED SUCCESSFULLY")
        else:
            print("BUG038: RETRY")
    except:
        print("BUG038: RETRY")

    # BUG039
    try:
        lst = ["hello", "world"]
        delimiter = " "
        result = join_strings(lst, delimiter)
        if result == "hello world":
            print("BUG039: SOLVED SUCCESSFULLY")
        else:
            print("BUG039: RETRY")
    except:
        print("BUG039: RETRY")

    # BUG040
    try:
        s = "hello world"
        result = title_case(s)
        if result == "Hello World":
            print("BUG040: SOLVED SUCCESSFULLY")
        else:
            print("BUG040: RETRY")
    except:
        print("BUG040: RETRY")


if __name__ == "__main__":
    test()
