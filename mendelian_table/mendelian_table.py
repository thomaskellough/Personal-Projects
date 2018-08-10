import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import logging
import platform
import os
import sys

logging.disable(logging.CRITICAL)
logging.basicConfig(level=logging.DEBUG,
                    format='%(funcName)s - %(levelname)s: %(message)s')


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


# Dictionary that holds phenotypes and genotypes off offspring
allele_count = {
    'Round, yellow seeds': [0, 'RRYY', 'RYYr', 'RRYy', 'RYry'],
    'Round, green seeds': [0, 'RRyy', 'Rryy'],
    'Wrinkled, yellow seeds': [0, 'YYrr', 'Yrry'],
    'Wrinkled, green seeds': [0, 'rryy']}


# Create GUI
class MendelianFrame:

    def display_genotypes(self, g1=None, g2=None, g3=None, g4=None):
        if g1 is None:
            g1 = self.p1_g1_var.get()
        if g2 is None:
            g2 = self.p2_g1_var.get()
        if g3 is None:
            g3 = self.p1_g2_var.get()
        if g4 is None:
            g4 = self.p2_g2_var.get()
        logging.debug('Entering mendelian function...')
        genotype = ''
        genotype_list = []
        i = 0
        for allele_1 in g1:
            for allele_2 in g2:
                for allele_3 in g3:
                    for allele_4 in g4:
                        temp_genotype = ''.join(allele_1 + allele_2 + allele_3 + allele_4)
                        temp_genotype = ''.join(sorted(''.join(temp_genotype), key=lambda c: (c.lower(), c)))
                        genotype += temp_genotype + '|'
                        genotype_list.append(temp_genotype)
                        logging.debug(f'Appended {temp_genotype} to list.')
                if i == 0:
                    self.genotype_1_var.set(genotype)
                elif i == 1:
                    self.genotype_2_var.set(genotype)
                elif i == 2:
                    self.genotype_3_var.set(genotype)
                elif i == 3:
                    self.genotype_4_var.set(genotype)
                genotype = ''
                i += 1
        sorted_genotypes = [''.join(sorted(_)) for _ in genotype_list]
        logging.debug(f'Calculating phenotypes.')
        for genotype in sorted_genotypes:
            for v in allele_count.values():
                if genotype in v:
                    logging.debug(f'Found {genotype} in {v}.')
                    v[0] += 1
        self.display_phenotypes()

    def display_phenotypes(self, g1=None, g2=None, g3=None, g4=None):
        max_length = 0  # For justification of phenotype printing
        for phenotype in allele_count.keys():
            if len(phenotype) > max_length:
                max_length = len(phenotype)
        if g1 is None:
            g1 = self.p1_g1_var.get()
        if g2 is None:
            g2 = self.p2_g1_var.get()
        if g3 is None:
            g3 = self.p1_g2_var.get()
        if g4 is None:
            g4 = self.p2_g2_var.get()
        count_list = list(allele_count.values())
        for i, key in enumerate(allele_count):
            if i == 0:
                self.phenotype_1_var.set(key.ljust(max_length) + ': ' + str(count_list[i][0]))
            elif i == 1:
                self.phenotype_2_var.set(key.ljust(max_length) + ': ' + str(count_list[i][0]))
            elif i == 2:
                self.phenotype_3_var.set(key.ljust(max_length) + ': ' + str(count_list[i][0]))
            elif i == 3:
                self.phenotype_4_var.set(key.ljust(max_length) + ': ' + str(count_list[i][0]))
        for v in allele_count.values():
            v[0] = 0

    def __init__(self, parent):
        root.title('Mendelian Dihibrid Cross')
        root.option_add('*tearOff', tk.FALSE)

        title_frame = tk.Frame(parent)
        title_frame.pack(fill='both')
        title_frame.columnconfigure(0, weight=1)

        upper_frame = tk.Frame(parent,
                               highlightcolor='darkblue',
                               highlightbackground='darkblue',
                               highlightthickness=5,
                               bd=10, bg='white')
        upper_frame.pack(expand=False, fill='x')

        lower_frame = tk.Frame(parent,
                               highlightbackground='darkblue',
                               highlightthickness=5,
                               bd=10, bg='white')
        lower_frame.pack(expand=True, fill='both')

        self.p1_g1_var = tk.StringVar(lower_frame)
        self.p1_g2_var = tk.StringVar(lower_frame)
        self.p2_g1_var = tk.StringVar(lower_frame)
        self.p2_g2_var = tk.StringVar(lower_frame)
        self.genotype_1_var = tk.StringVar(lower_frame)
        self.genotype_2_var = tk.StringVar(lower_frame)
        self.genotype_3_var = tk.StringVar(lower_frame)
        self.genotype_4_var = tk.StringVar(lower_frame)
        self.phenotype_1_var = tk.StringVar(lower_frame)
        self.phenotype_2_var = tk.StringVar(lower_frame)
        self.phenotype_3_var = tk.StringVar(lower_frame)
        self.phenotype_4_var = tk.StringVar(lower_frame)

        self.title_label = ttk.Label(title_frame,
                                     text='Welcome. This is a small program designed to test the different outcomes '
                                          'from a dihybrid cross. Each parent is represented by a different color. '
                                          'Select each genotype for each parent for each gene using the dropdown arrow',
                                     wraplength=600, justify='left', style='title.TLabel')
        self.title_label.grid(sticky=tk.NSEW)

        # Upper grid widgets
        self.title_label = ttk.Label(upper_frame, text='Dihybrid Cross', style='title.Label')
        self.cross_button = tk.Button(upper_frame, text='Cross', command=self.display_genotypes,
                                      font='helvatica 16 bold', relief='ridge', bg='gray90',
                                      width=10, activeforeground='darkblue', cursor='heart')
        self.y_label = ttk.Label(upper_frame, text='RRyy: (Round, green)\nrrYY: (wrinkled, yellow)', style='y.TLabel')
        self.x_label = ttk.Label(upper_frame, text='x', style='x.TLabel')
        self.p1_g1_options_menu = ttk.OptionMenu(upper_frame, self.p1_g1_var, 'RR', 'RR', 'Rr', 'rr',
                                                 style='p1_options.TMenubutton')
        self.p1_g2_options_menu = ttk.OptionMenu(upper_frame, self.p1_g2_var, 'YY', 'YY', 'Yy', 'yy',
                                                 style='p1_options.TMenubutton')
        self.p2_g1_options_menu = ttk.OptionMenu(upper_frame, self.p2_g1_var, 'rr', 'RR', 'Rr', 'rr',
                                                 style='p2_options.TMenubutton')
        self.p2_g2_options_menu = ttk.OptionMenu(upper_frame, self.p2_g2_var, 'yy', 'YY', 'Yy', 'yy',
                                                 style='p2_options.TMenubutton')

        # Upper grid placement
        self.title_label.grid(column=0, row=0, columnspan=4, sticky=tk.W)
        self.cross_button.grid(column=0, row=4, columnspan=4, sticky=tk.W)
        self.y_label.grid(column=0, row=2, columnspan=4, padx=5)
        self.x_label.grid(column=2, row=3, padx=10)
        self.p1_g1_options_menu.grid(column=0, row=3, sticky=tk.W)
        self.p1_g2_options_menu.grid(column=1, row=3, sticky=tk.W)
        self.p2_g2_options_menu.grid(column=3, row=3, sticky=tk.W)
        self.p2_g1_options_menu.grid(column=4, row=3, sticky=tk.W)

        # Lower grid widgets
        self.genotype_row_1_label = ttk.Label(lower_frame, textvariable=self.genotype_1_var, style='genotype.TLabel')
        self.genotype_row_2_label = ttk.Label(lower_frame, textvariable=self.genotype_2_var, style='genotype.TLabel')
        self.genotype_row_3_label = ttk.Label(lower_frame, textvariable=self.genotype_3_var, style='genotype.TLabel')
        self.genotype_row_4_label = ttk.Label(lower_frame, textvariable=self.genotype_4_var, style='genotype.TLabel')
        self.phenotype_1_label = ttk.Label(lower_frame, textvariable=self.phenotype_1_var, style='phenotype.TLabel')
        self.phenotype_2_label = ttk.Label(lower_frame, textvariable=self.phenotype_2_var, style='phenotype.TLabel')
        self.phenotype_3_label = ttk.Label(lower_frame, textvariable=self.phenotype_3_var, style='phenotype.TLabel')
        self.phenotype_4_label = ttk.Label(lower_frame, textvariable=self.phenotype_4_var, style='phenotype.TLabel')

        # Lower grid placement
        self.genotype_row_1_label.grid(column=0, row=4, sticky=tk.EW)
        self.genotype_row_2_label.grid(column=0, row=5, sticky=tk.EW)
        self.genotype_row_3_label.grid(column=0, row=6, sticky=tk.EW)
        self.genotype_row_4_label.grid(column=0, row=7, sticky=tk.EW)
        self.phenotype_1_label.grid(column=0, columnspan=4,  row=8, sticky=tk.EW)
        self.phenotype_2_label.grid(column=0, columnspan=4,  row=9, sticky=tk.EW)
        self.phenotype_3_label.grid(column=0, columnspan=4,  row=10, sticky=tk.EW)
        self.phenotype_4_label.grid(column=0, columnspan=4,  row=11, sticky=tk.EW)

        s = ttk.Style()
        s.configure('title.TLabel', font='helvetica 12 bold', background='darkblue', foreground='white')
        s.configure('p1_options.TMenubutton', font='helvetica 18 bold', foreground='darkblue', background='white')
        s.configure('p2_options.TMenubutton', font='helvetica 18 bold', foreground='red', background='white')
        s.configure('title.Label', font='helvetica 18 bold', background='white')
        s.configure('x.TLabel', font='helvetica 18 bold', background='white')
        s.configure('y.TLabel', font='helvetica 12 bold', background='white', foreground='gray20')
        s.configure('genotype.TLabel', font='Consolas 22', foreground='darkgreen', background='white', padding=5)
        s.configure('phenotype.TLabel', font='Consolas 20', foreground='darkblue', background='white', padding=5)

        main_menu = tk.Menu(root)
        root.config(menu=main_menu)
        sub_menu_file = tk.Menu(main_menu)
        sub_menu_help = tk.Menu(main_menu)

        main_menu.add_cascade(label='File', menu=sub_menu_file)
        sub_menu_file.add_command(label='Exit', command=root.quit)

        main_menu.add_cascade(label='Help', menu=sub_menu_help)
        sub_menu_help.add_command(label='License', command=display_license)


if __name__ == '__main__':
    root = tk.Tk()
    set_icon(root)
    frame = MendelianFrame(root)
    root.mainloop()
