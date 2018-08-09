#! python3
# random_student.py - randomly selects a student from a specified class period

import tkinter as tk
from tkinter import ttk
import random
from random import choice
import sys
import os
import logging
from PIL import Image
from PIL import ImageTk


# TODO: Create logging file for students

os.chdir(os.path.join(os.path.abspath('pictures')))

def restart_program():
    """Restarts the current program.
                Note: this function does not return. Any cleanup action (like
                saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)


def create_lists():
    single_list = [x for x in os.listdir('.') if x.startswith('single')]
    pair_list = [x for x in os.listdir('.') if x.startswith('pair')]
    group_list = [x for x in os.listdir('.') if x.startswith('group')]
    return single_list, pair_list, group_list

single_list, pair_list, group_list = create_lists()

# TODO: Create source file for student names
period_1 = ['Godric', 'Minerva', 'Harry', 'Ron', 'Hermione', 'Sir Nicholas', 'Albus', 'Dean', 'Seamus']
period_2 = ['Severus', 'Phineas', 'Tom Riddle', 'Horace', 'Crabbe', 'Goyle', 'Draco', 'Salazar', 'Pansy', 'Bellatrix']
period_3 = ['Newton', 'Nymphadora', 'Cedric', 'Hannah', 'Helga', 'Susan']
period_4 = ['Luna', 'Cho', 'Filius', 'Gilderoy', 'Rowena', 'Sybill', 'Moaning Myrtle', 'Penelope', 'Xenophilius']

# Create GUI
class NameFrame:

    def clear_shit(self):
        self.student_remove_list = []

    def display_image(self, image_list):
        image = random.choice(image_list)
        img = Image.open(image)
        base_width = 400
        width_percent = (base_width / float(img.size[0]))
        height_size = int((float(img.size[1]) * float(width_percent)))
        img = img.resize((base_width, height_size), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        self.label.configure(image=img)
        self.label.image = img
        image_list.remove(image)

    def class_select(self):
        class_list = self.class_select_var.get()
        if class_list == 'Period 1':
            return [x for x in period_1 if x not in self.student_remove_list]
        elif class_list == 'Period 2':
            return [x for x in period_2 if x not in self.student_remove_list]
        elif class_list == 'Period 3':
            return [x for x in period_3 if x not in self.student_remove_list]
        elif class_list == 'Period 4':
            return [x for x in period_4 if x not in self.student_remove_list]

    def random_student(self):
        try:
            class_list = self.class_select()
            length = 0 if len(class_list) - 1 < 0 else len(class_list) - 1
            self.length_class_names_var.set(f'Names left: {length}')
            student = random.choice(class_list)
            self.student_remove_list.append(student)
            self.display_name_var.set(student)
            self.display_image(single_list)
        except IndexError:
            class_list = self.class_select()
            self.length_class_names_var.set(f'Names left: {len(class_list)}')

    def random_pair(self):
        try:
            class_list = self.class_select()
            length = 0 if len(class_list) - 2 < 0 else len(class_list) - 2
            self.length_class_names_var.set(f'Names left: {length}')
            student1 = random.choice(class_list)
            class_list.remove(student1)
            student2 = random.choice(class_list)
            self.display_name_var.set('\n'.join([student1, student2]))
            self.student_remove_list.extend((student1, student2))
            self.display_image(pair_list)
        except IndexError:
            class_list = self.class_select()
            self.length_class_names_var.set(f'Names left: {len(class_list)}')

    def random_group(self):
        try:
            class_list = self.class_select()
            length = 0 if len(class_list) - 4 < 0 else len(class_list) - 4
            self.length_class_names_var.set(f'Names left: {length}')
            student1 = random.choice(class_list)
            class_list.remove(student1)
            student2 = random.choice(class_list)
            class_list.remove(student2)
            student3 = random.choice(class_list)
            class_list.remove(student3)
            student4 = random.choice(class_list)
            class_list.remove(student4)
            self.display_name_var.set('\n'.join([student1, student2, student3, student4]))
            self.student_remove_list.extend((student1, student2, student3, student4))
            self.display_image(group_list)
        except IndexError:
            class_list = self.class_select()
            self.length_class_names_var.set(f'Names left: {len(class_list)}')

    def __init__(self, parent):
        root.geometry('960x680')
        root.configure(background='#c2c2d6')
        title_frame = tk.Frame(parent, pady=20, background='#006600')
        select_frame = tk.Frame(parent, pady=20, background='#c2c2d6')
        display_frame = tk.Frame(parent, background='#c2c2d6')

        title_frame.grid(column=0, row=0, sticky=tk.EW)
        root.columnconfigure(0, weight=1)
        select_frame.grid(column=0, row=1, sticky=tk.EW)
        display_frame.grid(column=0, row=2)
        display_frame.columnconfigure(0, weight=1)

        self.student_remove_list = []

        self.class_select_var = tk.StringVar()
        self.display_name_var = tk.StringVar()
        self.length_class_names_var = tk.StringVar()
        self.label = tk.Label(display_frame, bg='#c2c2d6')
        self.label.grid(column=0, row=0, padx=50)

        self.class_select_dropdown = ttk.OptionMenu(select_frame, self.class_select_var,
                                                    'Period 1', 'Period 1', 'Period 2', 'Period 3', 'Period 4',
                                                    style='period.TMenubutton')
        self.length_class_names_label = ttk.Label(select_frame, textvariable=self.length_class_names_var, style='count_name.TLabel')
        self.title_label = ttk.Label(title_frame, text='Random Name Generator', style='title.TLabel')
        self.single_student_button = tk.Button(select_frame,
                                               text='Single',
                                               font='helvatica 20',
                                               background='red',
                                               foreground='white',
                                               width=10,
                                               command=self.random_student)
        self.pair_button = tk.Button(select_frame,
                                     text='Pair',
                                     font='helvatica 20',
                                     background='purple',
                                     foreground='white',
                                     width=10,
                                     command=self.random_pair)
        self.group_button = tk.Button(select_frame,
                                      text='Group',
                                      font='helvatica 20',
                                      background='orange',
                                      foreground='white',
                                      width=10,
                                      command=self.random_group)
        self.display_name_label = ttk.Label(display_frame, textvariable=self.display_name_var, style='display_name.TLabel')
        self.display_name_label.grid(column=1, row=0, padx=100)

        self.title_label.pack()
        self.class_select_dropdown.pack()
        self.length_class_names_label.pack()
        self.single_student_button.pack(side='left', expand=True, fill='x')
        self.pair_button.pack(side='left', expand=True, fill='x')
        self.group_button.pack(side='left', expand=True, fill='x')

        s = ttk.Style()
        s.configure('title.TLabel', font='Tahoma 42 bold', foreground='white', background='#006600')
        s.configure('count_name.TLabel', font='Tahoma 12 bold', foreground='#006600', background='#c2c2d6')
        s.configure('display_name.TLabel', font='Tahoma 40 bold', foreground='#006600', background='#c2c2d6')
        s.configure('period.TMenubutton', font='Tahoma 18', foreground='darkblue', background='#c2c2d6')
        s.configure('TButton', font='Tahoma 18 bold', foreground='darkblue', background='#c2c2d6')

        main_menu = tk.Menu(root)
        root.config(menu=main_menu)
        sub_menu_file = tk.Menu(main_menu)
        sub_menu_help = tk.Menu(main_menu)

        main_menu.add_cascade(label='File', menu=sub_menu_file)
        sub_menu_file.add_command(label='Clear Inputs', command=create_lists)
        sub_menu_file.add_separator()
        sub_menu_file.add_command(label='Exit', command=root.quit)

        main_menu.add_cascade(label='Help', menu=sub_menu_help)
        #sub_menu_help.add_command(label='How to use this program...', command=self.display_how_to)
        sub_menu_help.add_separator()
        #sub_menu_help.add_command(label='License', command=display_license)

        self.clear_button = tk.Button(select_frame, text='Clear', command=self.clear_shit)
        self.clear_button.pack()


if __name__ == '__main__':
    root = tk.Tk()
    frame = NameFrame(root)
    root.mainloop()

# TODO: refractor your damn code
