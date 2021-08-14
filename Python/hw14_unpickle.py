# Создать сотрудника Mary, пользуясь классом
# Employee и перенести его в другую программу,
# используя модуль Pickle и файловую систему.
# Узнать про + и - модуля Pickle.

# Import pickle module
import pickle

# Declare the employee class to store the value


class Employee:
    def __init__(self, name, email, position):
        self.name = name
        self.email = email
        self.position = position

    def display(self):
        print('Employee Information:')
        print('Name  :', self.name)
        print('Email  :', self.email)
        print('Position :', self.position)


# Open file for read data
fileDump = open('employeeDump', 'rb')

# Unpickle the data
employee = pickle.load(fileDump)

# Close file
fileDump.close()

# print the dataframe
employee.display()
