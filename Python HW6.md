## https://projecteuler.net/problem=36

The decimal number, 585 = 1001001001 in binary, is palindromic in both bases. Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2. (Please note that the palindromic number, in either base, may not include leading zeros.)

Напишите программу, которая решает описанную выше задачу и печатает ответ.

## Решение:
```
counter = 0  # ставим в 0 счетчик
for i in range(1, 1000000):  # проходим по диапазону
    str_i = str(i)  # десятичное в строку
    str_i_bin = str(bin(i)[2:])  # двоичное в строку и убираем 0b в начале
    inverse = str_i[::-1]  # перневорачиваем десятичное
    inverse_bin = str_i_bin[::-1]  # переворачиваем двоичное
    # проверяем на палиндромность
    if str_i == inverse and str_i_bin == inverse_bin:
        counter += i  # складываем, если палиндромы
print(counter)  # выводим результат
```
## Ответ:
```
PS C:\Users\borisov_sv\Documents\web\2021\css_2> & C:/Python39/python.exe c:/Users/borisov_sv/Documents/hw6.py
872187
```