def linear_search(lst, value):
    for i, v in enumerate(lst):
        if v == value:
            return i
    return -1
