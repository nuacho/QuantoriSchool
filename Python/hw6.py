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
