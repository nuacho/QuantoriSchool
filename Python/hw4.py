import re  # импортируем модуль регулярок
string = input("Input numbers:")  # запрашиваем строку с числами
# находим все числа, в т.ч. отрицательные, получаем список строк
result = re.findall(r'\-?\d+', string)
# print(result)
arr = [int(item) for item in result]  # генерируем список чисел из списка строк
print(sum(arr))  # печатаем сумму элементов списка чисел
