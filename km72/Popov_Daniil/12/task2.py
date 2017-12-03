l=[int(a) for a in input('Enter list: ').split()]
i=len(l)-1
counter = 0
def count_max(l,i):
    '''
    This function calculates the amount of list`s highest numbers

    Args:
        l - list of integers
        i - integer number, iterator

    Returns:
        counter - integer number

    Raises:
        ValueError

    Examples:
        >>> print(count_max([6,5,9,0,22,22,1]))
        2

        >>> print(find([5,4,a,b,c]))
        Traceback (most recent call last):
            ...
        ValueError
        
        
    '''
    global counter
    if l[i]==max(l):
        counter+=1
    if i==0:
        return counter
    if i != 0:
        return count_max(l,i-1)
print(count_max(l,i))
