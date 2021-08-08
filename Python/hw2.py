myString = input() # Вводим строку
myList = myString.split(" ") # преобразуем строку в список
mySet = list(set(myList)) # Преобразуем список в множество (оно содержит только уникальные значения)
print(' '.join(mySet)) # Выводим результат
