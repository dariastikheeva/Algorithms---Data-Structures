def linear_search(lst, value):
    indxs = []

    for i, v in enumerate(lst):
        if v == value:
            indxs.append(i)

    return indxs if indxs else -1
