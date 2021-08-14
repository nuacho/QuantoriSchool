# Создать сотрудника Mary, пользуясь классом
# Employee и перенести его в другую программу,
# используя модуль Pickle и файловую систему.
# Узнать про + и - модуля Pickle.

# Плюсы.
# 1. Сериализация позволяет сохранить некоторый прогресс на диске, выйти из программы и затем загрузить
# прогресс обратно после повторного открытия программы.
# 2. С помощью Pickle мы можем легко сериализовать очень большой спектр типов Python и, что немаловажно,
# пользовательские классы. Это означает, что нам не нужно создавать пользовательскую схему как в случае с JSON.
# 3.

# Минусы.
# 1. данные могут быть распакованы только с помощью Python. Кроме того, важно убедиться, что объекты обрабатываются
# с использованием той же версии Python, которая будет использоваться для их десериализации.
# 2. если мы сериализуем функцию, а затем распакуем ее в среде, где она либо не определена, либо не импортирована,
# возникнет исключение.
# 3. распаковка данных из ненадежного источника может привести к выполнению вредоносного фрагмента кода.


# Import pickle module
import pickle

# Declare the employee class to store the value


class Employee:
    def __init__(self, name, email, position):
        self.name = name
        self.email = email
        self.position = position


# Create employee  object
empObject = Employee('Mary', 'mary@gmail.com', 'Coordinator')

# Open file for store data
fileHandler = open('employeeDump', 'wb')

# Save the data into the file
pickle.dump(empObject, fileHandler)

# Close the file
fileHandler.close()

# Print message
print('Dump is created!')
