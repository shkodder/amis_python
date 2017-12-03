def find(max1, max2, list):
    '''
    This function finds the second highest number of a list

    Args:
        max1 - float number (current 1st highest)
        max2 - float number (current 2nd highest)
        list - list (excluding max1 & max2)

    Returns:
        max2 - float number (solution of the task)

    Raises:
        ValueError

    Examples:
        >>> print(find(6,5,[9,0,22,2]))
        9

        >>> print(find(5,4,[a,b,c]))
        Traceback (most recent call last):
            ...
        ValueError
        
        
    '''
    if len(list)==0:
        return max2
    first, rest = list[0], list[1:]
    if first > max1:
        return find(first, max1, rest)
    if first > max2:
        return find(max1, first, rest)
    return find(max1, max2, rest)

def second_highest(list):
    if len(list) < 2:
        raise ValueError("need more elements")
    a, b, rest = list[0], list[1], list[2:]
    if b > a:
        return find(b, a, rest)
    else:
        return find(a, b, rest)
l = [float(n) for n in input('Enter numbers: ').split()]

print(second_highest(l))
