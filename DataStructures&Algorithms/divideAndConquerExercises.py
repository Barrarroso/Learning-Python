"""Divide & Conquer Problems"""

def smallest_even_number(x: list) -> int:
    """Function that finds and returns the smallest even number in a python list. If the
    list does not contain even values, return None.
    """
    if x is None or len(x) == 0:
        return None

    #base case
    if len(x) == 1:
        return x[0] if x[0] % 2 == 0 else None

    m = len(x) // 2
    part1 = x[:m]
    part2 = x[m:]

    small1 = smallest_even_number(part1)
    small2 = smallest_even_number(part2)

    if small1 is not None and small2 is not None:
        return min(small1, small2)
    elif small1 is not None:
        return small1
    elif small2 is not None:
        return small2
    else:
        return None

def get_positions_of(_list: list, x: int) -> list:
    """Function that receives a list of integers and an integer x and returns a list with
    the positions (indexes) of x in that list. If x does not exist in the list, the function
    must return an empty list.
    """
    if _list is None or len(_list) == 0:
        return None

    return _get_positions_of(_list, x, 0, len(_list)-1)

def _get_positions_of(_list: list, x: int, start: int, end: int):

    if start > end:
        return

    if start == end:
        if _list[start] == x:
            return [start]
        else:
            return []

    m = (start+end)//2

    part1 = _get_positions_of(_list, x, start, m)
    part2 = _get_positions_of(_list, x, m+1, end)

    return part1 + part2


def sum_multiples_of(_list: list, x: int) -> int:
    """Function that receives a list of integers and an integer x and returns the sum of
    all multiples of x in list
    """

    if _list is None or len(_list) == 0:
        return 0

    if len(_list) == 1:
        is_multiple = _list[0]%x == 0
        return _list[0] if is_multiple else 0

    m = len(_list) // 2
    part1 = _list[:m]
    part2 = _list[m:]

    leftsum = sum_multiples_of(part1, x)
    rightsum = sum_multiples_of(part2, x)

    return leftsum + rightsum

def largest_smallest_of(_list: list) -> tuple:
    """Function that finds and returns the largest and smallest element of an array.
    """

    if _list is None or len(_list) == 0:
        return None

    if len(_list) == 1:
        return _list[0],_list[0]

    m = len(_list) // 2
    part1 = _list[:m]
    part2 = _list[m:]

    left_tuple = largest_smallest_of(part1)
    right_tuple = largest_smallest_of(part2)

    maxi = max(left_tuple[0], right_tuple[0])
    mini = min(left_tuple[1], right_tuple[1])

    return (maxi, mini)


def lowest_even_lowest_odd(_list: list) -> tuple:
    """Function that finds and returns the lowest even and the lowest odd element of
    an array.
    """

    if _list is None or len(_list) == 0:
        return

    if len(_list) == 1:
        if _list[0] % 2 == 0:
            #even
            return _list[0], None
        else:
            #odd
            return None, _list[0]

    m = len(_list) // 2
    part1 = _list[:m]
    part2 = _list[m:]

    even_odd_tuple1 = lowest_even_lowest_odd(part1)
    even_odd_tuple2 = lowest_even_lowest_odd(part2)

    #possible cases conquer
    # None, 2 and 2, None
    if even_odd_tuple1[0] and even_odd_tuple2[0]:
        minimum_even = min(even_odd_tuple1[0], even_odd_tuple2[0])
    elif even_odd_tuple1[0] is not None:
        minimum_even = even_odd_tuple1[0]
    elif even_odd_tuple2[0] is not None:
        minimum_even = even_odd_tuple2[0]
    else:
        minimum_even = None

    if even_odd_tuple1[1] and even_odd_tuple2[1]:
        minimum_odd = min(even_odd_tuple1[1], even_odd_tuple2[1])
    elif even_odd_tuple1[1] is not None:
        minimum_odd = even_odd_tuple1[1]
    elif even_odd_tuple2[1] is not None:
        minimum_odd = even_odd_tuple2[1]
    else:
        minimum_odd = None

    return minimum_even, minimum_odd

def binary_search(_list: list, x: int) -> int:
    """Implement a method based on divide and conquer strategy that
    takes a sorted Python List of numbers, A, and a number, x. The method must return the
    index of x in the list. If x is not found, the method returns -1.
    """
    if _list is None or len(_list) == 0:
        return

    return _binary_search(_list, x, 0, len(_list)-1)

def _binary_search(_list: list, x: int, start, end) -> int:
    if start>end:
        return -1

    m = (start+end)//2
    if _list[m] == x:
        return m

    elif _list[m] > x:
        #left half search
        return _binary_search(_list, x, start, m-1)
    elif _list[m] < x:
        #right half search
        return _binary_search(_list, x, m+1, end)

    #(1,3,7,10,20,25)

def occurences_of(s: str, c: str) -> int:
    """Implement a recursive function taking two parameters: a
    string, s, and a character, c. The method returns the number of occurrences of c in s.
    The solution must be based on the divide-and-conquer strategy (other approaches
    will not be evaluated).
    """
    if s is None or len(s) == 0:
        return

    if len(s) == 1:
        return 1 if s[0] == c else 0

    middle = len(s)//2
    part1 = s[:middle]
    part2 = s[middle:]

    occurences_left = occurences_of(part1, c)
    occurences_right = occurences_of(part2, c)
    return occurences_left + occurences_right

data = [1,3,1,2,-2,5,6,7,19,20,5,6,20,36]


print(smallest_even_number(data))

print(sum_multiples_of(data, 2))

print(largest_smallest_of(data))

print(lowest_even_lowest_odd(data))

print(get_positions_of(data, 5))

ordered_data = [1,3,4,10,20,25]

print(binary_search(ordered_data, 10))


mystring = "that is a phrase that has a lot of a's"
print(occurences_of(mystring,'a'))