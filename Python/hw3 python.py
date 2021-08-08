from collections import Counter  # импортируем класс Counter из модуля collections
words = input('Input some words:')  # получаем строку
myList = words.lower().split(" ")  # создаем список из words в нижнем регистре
# print(myList)
# из списка myList получаем класс Counter, содержащий словарь повторов значений списка
c = Counter(myList)
# print(dict(c))
# находим среди значений словаря максимальное значение
max_value = max(dict(c).values())
# выбираем ключи, соответствующие max_value
final_dict = {k: v for k, v in dict(c).items() if v == max_value}
# print(final_dict)

for k, v in final_dict.items():
    # печатаем эти максимальные значения с сепаратором "дефис"
    print(v, k, sep=' - ')
