# Напишите программу, которая читает данные из файлов
# /etc/passwd и /etc/group на вашей системе и выводит
# следующую информацию в файл output.txt:
# 1. Количество пользователей, использующих все имеющиеся
# интерпретаторы-оболочки.
# ( /bin/bash - 8 ; /bin/false - 11 ; ... )
# 2. Для всех групп в системе - UIDы пользователей
# состоящих в этих группах.
# ( root:1, sudo:1001,1002,1003, ...)
from collections import Counter
etc_passwd = "passwd"
etc_group = "group"

passwd = open(etc_passwd, mode='r', encoding="ascii")
group = open(etc_group, mode="r", encoding="ascii")

pwd_dict = {}
grp_dict = {}
pwd2_dict = {}


def shell():

    for line in passwd:
        for line2 in group:
            field2 = line2.split(":")
            # print(field2)
            grp_dict[field2[0]] = field2[3].strip()
        field = line.split(":")
        # print(field)
        pwd_dict[field[0]] = field[6].strip()
        pwd2_dict[field[0]] = field[2].strip()
    grp_new = {k: v for k, v in grp_dict.items() if v}
    pwd_new = {k: v for k, v in pwd2_dict.items() if v}

    # print(grp_new)
    # print(pwd_new)

    # print('\n-----------------', end='\n')

    print({k: pwd_new.get(v, v) for k, v in grp_new.items()})

    print('\n-----------------', end='\n')

    values = pwd_dict.values()
    counter = Counter(values)

    for k, v in dict(counter).items():
        print(k, v, sep=' - ', end='; ')


# passwd.close()
# group.close()
shell()
