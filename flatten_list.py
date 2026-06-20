def flatten_list(lst, flat_result=None):

    if flat_result is None:
        flat_result = []

    for item in lst:

        if type(item) is list:
            flatten_list(item, flat_result)

        else:
            flat_result.append(item)

    return flat_result


print(flatten_list([1, 2, [3], [4, 5]]))


print(flatten_list([1, [2], [3, [4, 5, [6]]], 7]))


print(flatten_list([1, 2, 3]))


print(flatten_list([]))
