## Встроенная функция input позволяет ожидать и возвращать данные из стандартного ввода ввиде строки (весь введенный пользователем текст до нажатия им enter).
Используя данную функцию, напишите программу, которая:

1. После запуска предлагает пользователю ввести неотрицательные целые числа,
разделенные через пробел и ожидает ввода от пользователя.
2. Находит наименьшее положительное число, не входящее в данный пользователем
список чисел и печатает его.


Например:
```
-> 2 1 8 4 2 3 5 7 10 18 82 2
6
```
## Решение:

```
# Создаем список значений, разделенных пробелом
A = [int(x) for x in input('Input numbers:').split()]
# A = set(inp_arr)
# print(sorted(A))


def solution(A):
    # создаем сет с отсортированным списком А
    a = frozenset(sorted(A))
    # находим максимальное значение
    m = max(a)

    if m > 0:  # если макс больше нуля
        for i in range(1, m):  # то проходим по всему набору
            if i not in a:  # если элемент не найден
                print(i)  # печатаем его как ответ
                return i
        else:
            print(m+1)  # если все числа в списке входят в набор, то ответ - макс +1
            return m+1
    else:
        return 1


solution(A)
```
### Вывод:
```
PS C:\Users\borisov_sv\Documents\web\2021\css_2> & C:/Python39/python.exe c:/Users/borisov_sv/Documents/hw5.py
Input numbers:1 2 3
4
```