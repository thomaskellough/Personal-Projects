#! python3
# random_student.py - randomly selects a student from a specified class period

import random
from random import choice
import sys
import os

os.chdir(r'C:\Users\tomal\Desktop\Python\MyPrograms')

class_list = sys.argv[1]

names = open('name_list.txt')
names = names.read().split('\n')
names = [name for name in names if name != '']


def random_students(number):
    student_list = [choice(names) for _ in range(number)]
    return student_list


def random_student(period):
    while True:
        input()
        student = random.choice(period)
        print(student, end='')
        period.remove(student)
        if len(period) == 0:
            return '\n\nEnd of program'


if sys.argv[1].lower() == 'period_1':
    period = ['Draco', 'Crabbe', 'Goyle', 'Marcus']
elif sys.argv[1].lower() == 'period_2':
    period = ['Harry', 'Ron', 'Hermione', 'Neville', 'Luna', 'Cho']
elif sys.argv[1].lower() == 'period_3':
    period = random_students(23)
elif sys.argv[1].lower() == 'period_4':
    period = random_students(25)
else:
    print('No class found.')
    sys.exit()

print(random_student(period))
