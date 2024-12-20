def merge(array1, array2):
    """
    Функция слияния двух отсортированных массивов в один.
    array1 и array2 - массивы представленные python-списками.
    """
    # Добавьте ваш код тут.
    new_array = []

    i = j = 0

    while i < len(array1) and j < len(array2):
        if array1[i] <= array2[j]:
            new_array.append(array1[i])
            i += 1
        else:
            new_array.append(array2[j])
            j += 1

    while i < len(array1):
        new_array.append(array1[i])
        i += 1

    while j < len(array2):
        new_array.append(array2[j])
        j += 1

    return new_array

array1 = [3, 4, 7, 8, 9]
array2 = [1, 5, 8]
array = merge(array1, array2)
print(array)