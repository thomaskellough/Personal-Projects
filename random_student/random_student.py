import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
import platform
import random
import logging
import os
import sys

# Disable only critical logs since they are for the programmer.
# Logs with the level debug are for creating the log file on how the
# students were grouped up.
logging.disable(logging.DEBUG)
logging.basicConfig(filename='Random Generator.log', level=logging.DEBUG,
                    format='%(funcName)s - %(asctime)s: %(message)s')


def set_icon(app):
    if platform.system() == "Windows":
        app.iconbitmap(resource_path(os.path.join("Assets", "icon.ico")))
    elif platform.system() == "Linux":
        imgicon = tk.PhotoImage(file=resource_path(os.path.join("Assets", "icon.gif")))
        app.tk.call("wm", "iconphoto", app._w, imgicon)


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def display_license():
    tk.messagebox.showinfo(
        message='The MIT License (MIT)\n'
                '=====================\n\n'
                'Copyright (c) 2018 Thomas Kellough\n\n'
                'Permission is hereby granted, free of charge, to any person obtaining a copy of\n'
                'this software and associated documentation files (the "Software"), to deal in\n'
                'the Software without restriction, including without limitation the rights to\n'
                'use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies\n'
                'of the Software, and to permit persons to whom the Software is furnished to do\n'
                'so, subject to the following conditions:\n\n'

                'The above copyright notice and this permission notice shall be included in all'
                'copies or substantial portions of the Software.\n\n'

                'THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n'
                'IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n'
                'FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n'
                'AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n'
                'LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n'
                'OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\n'
                'SOFTWARE.')


class_dict = {'Period_1': None, 'Period_2': None, 'Period_3': None, 'Period_4': None,
              'Period_5': None, 'Period_6': None, 'Period_7': None, 'Period_8': None}

logging.debug('Searching through directory for roster txt files')
for file in os.listdir('.'):
    if not file.__contains__('period'):
        continue
    for key in class_dict:
        if file.lower() == key.lower() + '.txt':
            f = open(file).readlines()
            class_dict[key] = (list(map(str.strip, f)))
            logging.debug(f'Found text file for {file}')
# Create lists of images
os.chdir(os.path.join(os.path.abspath('pictures')))

logging.debug('Searching through directory for pictures')
single_list = [x for x in os.listdir('.') if x.startswith('single')]
pair_list = [x for x in os.listdir('.') if x.startswith('pair')]
group_list = [x for x in os.listdir('.') if x.startswith('group')]
logging.debug(f'Created lists: Single List: {single_list}\nPair List:{pair_list}\nGroup List:{group_list}')


# GUI class
class NameFrame:

    def reset_names(self):
        self.student_remove_list = []

    def display_image(self, image_list):
        logging.debug('Displaying the image and name...')
        image = random.choice(image_list)
        img = Image.open(image)
        base_width = 500
        width_percent = (base_width / float(img.size[0]))
        height_size = int((float(img.size[1]) * float(width_percent)))
        logging.debug(f'Resizing {image} from {img.size} to {base_width, height_size}')
        img = img.resize((base_width, height_size), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        self.display_frame_bg.configure(image=img, pady=15)
        self.display_frame_bg.image = img
        image_list.remove(image)

    def class_select(self):
        logging.debug('Selecting the class...')
        class_list = self.class_select_var.get()
        if class_list == 'Period 1':
            return [x for x in class_dict['Period_1'] if x not in self.student_remove_list]
        elif class_list == 'Period 2':
            return [x for x in class_dict['Period_2'] if x not in self.student_remove_list]
        elif class_list == 'Period 3':
            return [x for x in class_dict['Period_3'] if x not in self.student_remove_list]
        elif class_list == 'Period 4':
            return [x for x in class_dict['Period_4'] if x not in self.student_remove_list]
        elif class_list == 'Period 5':
            return [x for x in class_dict['Period_5'] if x not in self.student_remove_list]
        elif class_list == 'Period 6':
            return [x for x in class_dict['Period_6'] if x not in self.student_remove_list]
        elif class_list == 'Period 7':
            logging.info(f'Choosing from {class_list}')
            return [x for x in class_dict['Period_7'] if x not in self.student_remove_list]
        elif class_list == 'Period 8':
            logging.info(f'Choosing from {class_list}')
            return [x for x in class_dict['Period_8'] if x not in self.student_remove_list]

    def random_student(self):
        try:
            logging.debug(f'Selecting a random student...')
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
            logging.info(f'Selecting from {self.class_select_var.get()}')
            logging.info(f'Pair of students for: {student1} with {student2}')
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
            logging.info(f'Selecting from {self.class_select_var.get()}')
            logging.info(f'Group: {student1}, {student2}, {student3}, {student4}')
            self.display_name_var.set('\n'.join([student1, student2, student3, student4]))
            self.student_remove_list.extend((student1, student2, student3, student4))
            self.display_image(group_list)
        except IndexError:
            class_list = self.class_select()
            self.length_class_names_var.set(f'Names left: {len(class_list)}')

    def __init__(self, parent):
        root.geometry('960x680')
        root.configure(background='#c2c2d6')
        root.title('Random Name Generator')

        title_frame = tk.Frame(parent, pady=20, background='#006600')
        select_frame = tk.Frame(parent, pady=20, background='#c2c2d6')
        display_frame_left = tk.Frame(parent, background='#c2c2d6')
        display_frame_right = tk.Frame(parent, background='#c2c2d6')

        title_frame.grid(column=0, row=0, sticky=tk.EW, columnspan=2)
        select_frame.grid(column=0, row=1, sticky=tk.EW, columnspan=2)
        display_frame_left.grid(column=0, row=2, sticky=tk.W)
        display_frame_right.grid(column=1, row=2, sticky=tk.W)

        root.columnconfigure(0, weight=1)
        display_frame_left.columnconfigure(0, weight=1)

        self.student_remove_list = []
        self.class_select_var = tk.StringVar()
        self.display_name_var = tk.StringVar()
        self.length_class_names_var = tk.StringVar()

        # Rename class list for display on tkinter. Used in class select dropdown
        self.class_list_select = [x.replace('_', ' ') for x in class_dict.keys() if class_dict[x] is not None]

        # Create widgets
        self.title_label = ttk.Label(title_frame, text='Random Name Generator', style='title.TLabel')
        self.class_select_dropdown = ttk.OptionMenu(select_frame,
                                                    self.class_select_var,
                                                    self.class_list_select[0],
                                                    *self.class_list_select,
                                                    style='period.TMenubutton')
        self.length_class_names_label = ttk.Label(select_frame,
                                                  textvariable=self.length_class_names_var,
                                                  style='count_name.TLabel')
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
        self.reset_button = tk.Button(select_frame,
                                      text='Reset',
                                      font='helvatica 12',
                                      background='#c2c2d6',
                                      foreground='black',
                                      command=self.reset_names)

        self.display_name_label = ttk.Label(display_frame_right,
                                            textvariable=self.display_name_var,
                                            style='display_name.TLabel')
        self.display_frame_bg = tk.Label(display_frame_left, bg='#c2c2d6')

        # Pack and grid widgets
        self.title_label.pack()
        self.reset_button.pack()
        self.length_class_names_label.pack()
        self.class_select_dropdown.pack()
        self.single_student_button.pack(side='left', expand=True, fill='x')
        self.pair_button.pack(side='left', expand=True, fill='x')
        self.group_button.pack(side='left', expand=True, fill='x')
        self.display_name_label.grid(column=1, row=0, padx=50)
        self.display_frame_bg.grid(column=0, row=0)

        # Configure styles
        s = ttk.Style()
        s.configure('title.TLabel', font='Tahoma 42 bold', foreground='white', background='#006600')
        s.configure('count_name.TLabel', font='Tahoma 12 bold', foreground='#006600', background='#c2c2d6')
        s.configure('display_name.TLabel', font='Tahoma 40 bold', foreground='#006600', background='#c2c2d6')
        s.configure('period.TMenubutton', font='Tahoma 18', foreground='darkblue', background='#c2c2d6')
        s.configure('TButton', font='Tahoma 18 bold', foreground='darkblue', background='#c2c2d6')

        # Create menus
        root.option_add('*tearOff', tk.FALSE)
        main_menu = tk.Menu(root)
        root.config(menu=main_menu)
        sub_menu_file = tk.Menu(main_menu)
        sub_menu_help = tk.Menu(main_menu)

        main_menu.add_cascade(label='File', menu=sub_menu_file)
        sub_menu_file.add_command(label='Reset', command=self.reset_names)
        sub_menu_file.add_separator()
        sub_menu_file.add_command(label='Exit', command=root.quit)

        main_menu.add_cascade(label='Help', menu=sub_menu_help)
        sub_menu_help.add_command(label='License', command=display_license)


if __name__ == '__main__':
    root = tk.Tk()
    os.chdir('..')
    set_icon(root)
    os.chdir(os.path.join(os.path.abspath('.'), 'pictures'))
    frame = NameFrame(root)
    root.mainloop()
