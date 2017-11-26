def setList():
    '''
    This function gets numbers from a user and sets a list

    Args:
        -

    Returns:
        num_list - generated list user's input (will be used in findMin function)

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
            print('вводите только числа')
    return numbers
setList()
def findMin(l):
    '''
    This function finds the least element of the list

    Args:
        l - list

    Returns:
        float number

    Raises:
        -

    Examples:
        >>> print(findMin([18, -209, 7])
        [-209]
    '''
    if len(l) == 1:
       return l[0]

    else:
       return min(l[0], findMin(l[1:]))
print(findMin(numbers))

