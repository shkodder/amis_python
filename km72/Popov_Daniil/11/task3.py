def setList():
    '''
    This function gets numbers from a user and sets a list

    Args:
        -

    Returns:
        num_list - generated list user's input (will be used in reverse function)

    Raises:
        -

    Examples:
        >>> print(setList())
        сколько чисел вы хотите задать? <user_input>
        введите число <input_1>
        .
        .
        .
        введите число <input_n>
        [<input_1> ... <input_n>]
    '''
    global numbers
    numbers=[]
    while True:
        try:
            for i in range(int(input('сколько чисел вы хотите задать? '))):
                numbers.append([float(input('введите число '))])
            break
        except ValueError:
            print('вводите тоько числа')
    return numbers
setList()
def reverse(l):
    '''
    This function reverses the elements of the list

    Args:
        l - list

    Returns:
        list(reversed)

    Raises:
        -

    Examples:
        >>> print(reverse([1, 2.4, 34, -5, 99]))
        [99.0, -5.0, 34.0, 2.4, 1.0]
    '''
    if (len(l) < 2):
        return l
    else:
        mid = len(l)//2
        return (reverse(l[mid:]) + reverse(l[:mid]))
print(reverse(numbers))
