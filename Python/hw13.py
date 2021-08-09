# Напишите функцию, которая переводит значения показаний
# температуры из Цельсия в Фаренгейт и наоборот.
# hw13: функция должны быть максимально удобной в использовании.

def temp_calc():
    temp = int(input('Input temperature:'))
    corf = (input('C or F')).lower()

    if corf == 'c':
        fahrenheit = (temp * 9 / 5) + 32
        print('Temp in F = ' + str(round(fahrenheit, 1)))
    elif corf == 'f':
        celsius = (temp - 32) * 5 / 9
        print('Temp in C = ' + str(round(celsius, 1)))
    else:
        print('Type F or C please')


temp_calc()
