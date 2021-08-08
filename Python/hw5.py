
# string = input("Input numbers:")  # запрашиваем строку с числами


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
