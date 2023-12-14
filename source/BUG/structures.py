def add_to_list(lst: list, element: int) -> list:
    """
    BUG061: add_to_list should add the element to the end of the list, not to the beginning.
    """
    lst.insert(0, element)
    return lst


def remove_from_list(lst: list, element: int) -> list:
    """
    BUG062: remove_from_list should remove the first occurrence of the element from the list, not the first element.
    """
    lst.pop(0)
    return lst


def get_list_length(lst: list) -> int:
    """
    BUG063: get_list_length should return the length of the list, not the last element.
    """
    result = lst[-1]
    return result


def concatenate_lists(lst1: list, lst2: list) -> list:
    """
    BUG064: concatenate_lists should concatenate two lists, not append the second list to the first.
    """
    lst1.append(lst2)
    return lst1


def get_list_sum(lst: list) -> int:
    """
    BUG065: get_list_sum should return the sum of the elements in the list, not the length.
    """
    result = len(lst)
    return result


def multiply_list_elements(lst: list, factor: int) -> list:
    """
    BUG066: multiply_list_elements should multiply each element in the list by the factor, not append the factor.
    """
    lst.append(factor)
    return lst


def find_max_in_list(lst: list) -> int:
    """
    BUG067: find_max_in_list should return the maximum value in the list, not the length.
    """
    result = len(lst)
    return result


def count_occurrences(lst: list, element: int) -> int:
    """
    BUG068: count_occurrences should return the number of occurrences of the element in the list, not the length.
    """
    result = len(lst)
    return result


def sort_list_descending(lst: list) -> list:
    """
    BUG069: sort_list_descending should sort the list in descending order, not in ascending order.
    """
    lst.sort()
    return lst


def reverse_list(lst: list) -> list:
    """
    BUG070: reverse_list should reverse the order of elements in the list, not sort it in descending order.
    """
    lst.reverse()
    return lst


def get_unique_elements(lst: list) -> list:
    """
    BUG071: get_unique_elements should return a list of unique elements, not the same list.
    """
    temp = []
    for element in lst:
        if element not in temp:
            temp.append (element)
    result = temp
    return result


def create_dictionary(keys: list, values: list) -> dict:
    """
    BUG072: create_dictionary should create a dictionary from the given keys and values, not concatenating them.
    """
    result = dict()
    for i in range(0, len(keys)):
        result[keys[i]] = values[i]
    return result


def get_dict_value(dictionary: dict, key: str) -> str:
    """
    BUG073: get_dict_value should return the value associated with the key in the dictionary, not the key itself.
    """
    result = dictionary[key]
    return result


def add_to_dict(dictionary: dict, key: str, value: str) -> dict:
    """
    BUG074: add_to_dict should add a key-value pair to the dictionary, not remove the key-value pair.
    """
    dictionary.pop(key)
    return dictionary


def remove_from_dict(dictionary: dict, key: str) -> dict:
    """
    BUG075: remove_from_dict should remove the key-value pair from the dictionary, not add a new key-value pair.
    """
    dictionary[key] = 1
    return dictionary


def get_dict_keys(dictionary: dict) -> list:
    """
    BUG076: get_dict_keys should return a list of keys in the dictionary, not the values.
    """
    result = list(dictionary.values())
    return result


def get_dict_values(dictionary: dict) -> list:
    """
    BUG077: get_dict_values should return a list of values in the dictionary, not the keys.
    """
    result = list(dictionary.keys())
    return result


def merge_dicts(dict1: dict, dict2: dict) -> dict:
    """
    BUG078: merge_dicts should merge two dictionaries, not overwrite values from the first dictionary with the second.
    """
    result = dict1.update(dict2)
    return result


def clear_dict(dictionary: dict) -> dict:
    """
    BUG079: clear_dict should remove all items from the dictionary, not just the first.
    """
    dictionary.popitem()
    return dictionary


def is_key_in_dict(dictionary: dict, key: str) -> bool:
    """
    BUG080: is_key_in_dict should return True if the key is in the dictionary, not if it's not.
    """
    result = not key in dictionary
    return result


def test():
    # BUG061
    try:
        lst = [1, 2, 3]
        element = 4
        result = add_to_list(lst, element)
        if result == [1, 2, 3, 4]:
            print("BUG061: SOLVED SUCCESSFULLY")
        else:
            print("BUG061: RETRY")
    except:
        print("BUG061: RETRY")

    # BUG062
    try:
        lst = [1, 2, 3, 2]
        element = 2
        result = remove_from_list(lst, element)
        if result == [1, 3, 2]:
            print("BUG062: SOLVED SUCCESSFULLY")
        else:
            print("BUG062: RETRY")
    except:
        print("BUG062: RETRY")

    # BUG063
    try:
        lst = [1, 2, 9, 8, 1]
        result = get_list_length(lst)
        if result == 5:
            print("BUG063: SOLVED SUCCESSFULLY")
        else:
            print("BUG063: RETRY")
    except:
        print("BUG063: RETRY")

    # BUG064
    try:
        lst1 = [1, 2, 3]
        lst2 = [4, 5, 6]
        result = concatenate_lists(lst1, lst2)
        if result == [1, 2, 3, 4, 5, 6]:
            print("BUG064: SOLVED SUCCESSFULLY")
        else:
            print("BUG064: RETRY")
    except:
        print("BUG064: RETRY")

    # BUG065
    try:
        lst = [1, 2, 3]
        result = get_list_sum(lst)
        if result == 6:
            print("BUG065: SOLVED SUCCESSFULLY")
        else:
            print("BUG065: RETRY")
    except:
        print("BUG065: RETRY")

    # BUG066
    try:
        lst = [1, 2, 3]
        factor = 2
        result = multiply_list_elements(lst, factor)
        if result == [2, 4, 6]:
            print("BUG066: SOLVED SUCCESSFULLY")
        else:
            print("BUG066: RETRY")
    except:
        print("BUG066: RETRY")

    # BUG067
    try:
        lst = [1, 2, 3, 2, 1]
        result = find_max_in_list(lst)
        if result == 3:
            print("BUG067: SOLVED SUCCESSFULLY")
        else:
            print("BUG067: RETRY")
    except:
        print("BUG067: RETRY")

    # BUG068
    try:
        lst = [1, 2, 3, 2]
        element = 2
        result = count_occurrences(lst, element)
        if result == 2:
            print("BUG068: SOLVED SUCCESSFULLY")
        else:
            print("BUG068: RETRY")
    except:
        print("BUG068: RETRY")

    # BUG069
    try:
        lst = [2, 1, 3]
        result = sort_list_descending(lst)
        if result == [3, 2, 1]:
            print("BUG069: SOLVED SUCCESSFULLY")
        else:
            print("BUG069: RETRY")
    except:
        print("BUG069: RETRY")

    # BUG070
    try:
        lst = [2, 1, 3]
        result = reverse_list(lst)
        if result == [3, 1, 2]:
            print("BUG070: SOLVED SUCCESSFULLY")
        else:
            print("BUG070: RETRY")
    except:
        print("BUG070: RETRY")

    # BUG071
    try:
        lst = [1, 2, 2, 3, 3]
        result = get_unique_elements(lst)
        if result == [1, 2, 3]:
            print("BUG071: SOLVED SUCCESSFULLY")
        else:
            print("BUG071: RETRY")
    except:
        print("BUG071: RETRY")

    # BUG072
    try:
        keys = ['a', 'b', 'c']
        values = [1, 2, 3]
        result = create_dictionary(keys, values)
        if result == {'a': 1, 'b': 2, 'c': 3}:
            print("BUG072: SOLVED SUCCESSFULLY")
        else:
            print("BUG072: RETRY")
    except:
        print("BUG072: RETRY")

    # BUG073
    try:
        dictionary = {'a': 1, 'b': 2, 'c': 3}
        key = 'a'
        result = get_dict_value(dictionary, key)
        if result == 1:
            print("BUG073: SOLVED SUCCESSFULLY")
        else:
            print("BUG073: RETRY")
    except:
        print("BUG073: RETRY")

    # BUG074
    try:
        dictionary = {'a': 1, 'b': 2}
        key = 'c'
        value = 3
        result = add_to_dict(dictionary, key, value)
        if result == {'a': 1, 'b': 2, 'c': 3}:
            print("BUG074: SOLVED SUCCESSFULLY")
        else:
            print("BUG074: RETRY")
    except:
        print("BUG074: RETRY")

    # BUG075
    try:
        dictionary = {'a': 1, 'b': 2, 'c': 3}
        key = 'a'
        result = remove_from_dict(dictionary, key)
        if result == {'b': 2, 'c': 3}:
            print("BUG075: SOLVED SUCCESSFULLY")
        else:
            print("BUG075: RETRY")
    except:
        print("BUG075: RETRY")

    # BUG076
    try:
        dictionary = {'a': 1, 'b': 2, 'c': 3}
        result = get_dict_keys(dictionary)
        if result == ['a', 'b', 'c']:
            print("BUG076: SOLVED SUCCESSFULLY")
        else:
            print("BUG076: RETRY")
    except:
        print("BUG076: RETRY")

    # BUG077
    try:
        dictionary = {'a': 1, 'b': 2, 'c': 3}
        result = get_dict_values(dictionary)
        if result == [1, 2, 3]:
            print("BUG077: SOLVED SUCCESSFULLY")
        else:
            print("BUG077: RETRY")
    except:
        print("BUG077: RETRY")

    # BUG078
    try:
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        result = merge_dicts(dict1, dict2)
        if result == {'a': 1, 'b': 3, 'c': 4}:
            print("BUG078: SOLVED SUCCESSFULLY")
        else:
            print("BUG078: RETRY")
    except:
        print("BUG078: RETRY")

    # BUG079
    try:
        dictionary = {'a': 1, 'b': 2, 'c': 3}
        result = clear_dict(dictionary)
        if result == {}:
            print("BUG079: SOLVED SUCCESSFULLY")
        else:
            print("BUG079: RETRY")
    except:
        print("BUG079: RETRY")

    # BUG080
    try:
        dictionary = {'a': 1, 'b': 2, 'c': 3}
        key = 'a'
        result = is_key_in_dict(dictionary, key)
        if result is True:
            print("BUG080: SOLVED SUCCESSFULLY")
        else:
            print("BUG080: RETRY")
    except:
        print("BUG080: RETRY")


if __name__ == "__main__":
    test()
