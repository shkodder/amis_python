def power(a, n):
    if n>1:
        return a*power(a, n-1)  #функція power рекурсивно викликає саму себе
    elif n==1:
        return a
print(power(float(input('enter a ')), int(input('enter n '))))
