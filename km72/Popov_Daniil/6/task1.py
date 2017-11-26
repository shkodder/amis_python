from math import sqrt
def distance(x1, y1, x2, y2):                  # х1, х2, у1, у2 - локальні змінні
    result = sqrt(((x2-x1)**2)+((y2-y1)**2))   #формула обчислення відстані між двома точкми на координатній площині
    return result                              #повернення результату
print(distance(float(input('enter x1 ')), float(input('enter y1 ')), float(input('enter x2 ')), float(input('enter y2 ')))) #задання коодинат користувачем
