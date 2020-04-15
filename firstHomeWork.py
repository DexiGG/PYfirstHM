#7.04.20
#1
import math

print("Формула квадратного уравнения (ax^2 + bx + c = 0):")
a = 1
b = 5
c = 1

discr = b ** 2 - 4 * a * c
print("Дискриминант D = %.2f" % discr)

if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif discr == 0:
    x = -b / (2 * a)
    print("x = %.2f" % x)
else:
    print("Корней нет")

#2
print("Формула плозади S=pi*r^2")
r = 5
S = math.pi * 5 ** 2
print("Площадь треугольника S= %.2f" % S)

#3
s = 'Hello world'
print('Второй символ = ' + s[1])
print('Предпоследний символ = ' + s[-2])
#4
print('Количество элементов')
print(s.count('') - 1)
print('Верхний регистр = ' + s.upper())

def capitalize(s):
    for x in s[:].split():
        s = s.replace(x, x.capitalize())

    return (s)
print('Только заглавными = ' + capitalize(s))
#5
#help([object])
#6
string = 'Hello World'
number = 142141
print(type(string))
print(type(number))