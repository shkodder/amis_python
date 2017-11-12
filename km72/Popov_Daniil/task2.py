from math import pow
def power(a, n):
    result = pow(a, n) #використання вбудованої функції
    return result      #повернення результату
print(power(float(input('enter a ')), int(input('enter n '))))  # а - дійсне додатнє, n - ціле
