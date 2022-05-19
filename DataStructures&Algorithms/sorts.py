def quicksort(_list: list):
    if _list is None or len(_list) == 0:
        return

    return _quicksort(_list, 0, len(_list) - 1)

def _quicksort(_list: list, l, r):
    if l >= r:
        return

    pivot = partition(_list, l, r)
    #sort left
    _quicksort(_list, l, pivot - 1)
    #sort right
    _quicksort(_list, pivot + 1, r)


def partition(_list, l, r):
    #picks the pivot at the end at first
    pivot = _list[r]
    #returns the pivot to achieve quicksort
    i = l - 1
    for j in range(l, r):
        if _list[j] < pivot:
            i += 1
            #swap elems
            _list[j], _list[i] = _list[i], _list[j]

    _list[i+1], _list[r] = _list[r], _list[i+1]
    return i + 1

a = [3, -2, -1, 0, 2, 4, 1]

quicksort(a)

print(a)

def quicksortm(data):
    #quicksort with pivot element in the middle
    if data is None or len(data) == 0:
        return

    return _quicksortm(data, 0, len(data) -1)

def _quicksortm(data, left, right):
    i = left
    j = right
    m=(left + right) // 2
    p = data[m] # pivot element in the middle
    if i <= j: # if left index < right index
        while data[i] < p:
            i += 1
        while data[j] >= p:
            j -= 1
        if i <= j:
            data[i], data[j] = data[j], data[i] # swap
            i += 1
            j -= 1
        if left < j: # sort left list
            _quicksort(data, left, j)
        if i < right: # sort right list
            _quicksort(data, i, right)
    return data

a = [3, -2, -1, 0, 2, 4, 1]

quicksortm(a)

print(a)