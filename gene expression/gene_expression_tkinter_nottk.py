from random import choice
from tkinter import *
import tkinter.messagebox
import logging
import re


logging.basicConfig(filename='gene_expression.log', level=logging.DEBUG,
                    format='%(funcName)s - %(levelname)s: %(message)s')
logging.disable(logging.CRITICAL)

nucleotide_list = ['A', 'T', 'G', 'C']
start_codon = 'AUG'
stop_codon = ['UAA', 'UAG', 'UGA']

mRNA_dict = {'A': 'U',
             'T': 'A',
             'G': 'C',
             'C': 'G'}

tRNA_dict = {'A': 'U',
             'U': 'A',
             'C': 'G',
             'G': 'C'}

codon_dict = {'Phe': ['UUU', 'UUC'],
              'Leu': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],
              'Ile': ['AUU', 'AUC', 'AUA'],
              'Met': ['AUG'],
              'Val': ['GUU', 'GUC', 'GUA', 'GUG'],
              'Ser': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],
              'Pro': ['CCU', 'CCC', 'CCA', 'CCG'],
              'Thr': ['ACU', 'ACC', 'ACA', 'ACG'],
              'Ala': ['GCU', 'GCC', 'GCA', 'GCG'],
              'Tyr': ['UAU', 'UAC'],
              'His': ['CAU', 'CAC'],
              'Gln': ['CAA', 'CAG'],
              'Asn': ['AAU', 'AAC'],
              'Lys': ['AAA', 'AAG'],
              'Asp': ['GAU', 'GAC'],
              'Glu': ['GAA', 'GAG'],
              'Cys': ['UGU', 'UGC'],
              'Trp': ['UGG'],
              'Arg': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
              'Gly': ['GGU', 'GGC', 'GGA', 'GGG'],
              'STOP': ['UAA', 'UAG', 'UGA']}


def dict_to_list(dict_of_codons):
    return [[k, v] for k, v in dict_of_codons.items()]


def create_random_sequence(number):
    sequence = ''.join(choice(nucleotide_list) for _ in range(number))
    return sequence


def transcribe(sequence):
    return ''.join(mRNA_dict[nucleotide] for nucleotide in sequence)


def mRNA_to_tRNA(sequence):
    return ''.join(tRNA_dict[nucleotide] for nucleotide in sequence)


def translate(sequence):
    try:
        logging.debug('Beginning translation...')
        # Find start codon
        logging.debug('Searching for start codon...')
        start_index = sequence.index(start_codon)
        start_peptide_chain = sequence[start_index:]
        logging.debug(f'Peptide chain from start codon.\n{start_peptide_chain}')

        # Find stop codon
        logging.debug('Searching for stop codon...')
        peptide_chain = []
        for nucleotide in range(0, len(start_peptide_chain), 3):
            codon = start_peptide_chain[nucleotide] \
                    + start_peptide_chain[nucleotide + 1] \
                    + start_peptide_chain[nucleotide + 2]
            peptide_chain.append(codon)
            if codon in stop_codon:
                break
        logging.debug(f'Peptide chain after finding stop codon.\n{peptide_chain}')

        # Determine amino acid
        logging.debug('Creating amino acid list')
        amino_acids = {n:k for k, v in codon_dict.items() for n in v}
        amino_acids_list = [amino_acids[codon] for codon in peptide_chain]
        logging.debug(f'List of amino acids:\n{amino_acids_list}')

        # Return a string of amino acids
        logging.debug('Converting amino acid list to a string')
        aa_string = '-'.join(amino_acids_list)
        logging.debug(f'String of amino acids.\n{aa_string}')
        return aa_string
    except (IndexError, ValueError):
        return 'No protein found'


# Creating GUI
class MyFrame:

    def display_license(self):
        tkinter.messagebox.showinfo(
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

    def make_menu(self, widg):
        self.popup_menu = tkinter.Menu(widg)
        self.popup_menu.add_command(label="Cut")
        self.popup_menu.add_command(label="Copy")
        self.popup_menu.add_command(label="Paste")

    def show_menu(self, x):
        w = x.widget
        self.popup_menu.entryconfigure("Cut", command=lambda: w.event_generate("<<Cut>>"))
        self.popup_menu.entryconfigure("Copy", command=lambda: w.event_generate("<<Copy>>"))
        self.popup_menu.entryconfigure("Paste", command=lambda: w.event_generate("<<Paste>>"))
        self.popup_menu.tk.call("tk_popup", self.popup_menu, x.x_root, x.y_root)

    def clear_screen(self):
        self.random_entry.delete(0, 'end')
        self.mRNA_entry.delete(0, 'end')
        self.mRNA_to_tRNA_entry.delete(0, 'end')
        self.translate_entry.delete(0, 'end')

    def display_how_to(self):
        tkinter.messagebox.showinfo(
            message="Welcome. This is a small program designed to let you practice your skills with transcription and "
                    "translation. It's separated into four parts. The first section allows you to either enter your "
                    "own DNA strand or calculate a random sequence. The next step allows you to input an mRNA strand "
                    "strand based off the DNA sequence. Then you can check your answer with the button to the right. "
                    "Repeat these steps for the tRNA sequence and then the specific amino-acid sequence.")

    def create_rand_seq(self, event):
        var = self.rand_seq_length.get()
        try:
            if int(var) > 2000:
                tkinter.messagebox.showinfo(message='Please enter less a number less than 2000.')
                return
        except ValueError:
            tkinter.messagebox.showerror(title='Error', message='Please ensure you enter a valid number of '
                                                                'nucletodides.')
            return
        try:
            self.rand_entry_var.set(create_random_sequence(int(var)).upper())
        except KeyError:
            tkinter.messagebox.showerror(title='Error', message='Please ensure you only enter nucletodides.')

    def create_mRNA_tk(self, event):
        try:
            self.mRNA_var.set(transcribe(self.rand_entry_var.get().upper()))
        except KeyError:
            tkinter.messagebox.showerror(title='Error', message='Please ensure you only enter nucletodides.')

    def mRNA_to_tRNA_tk(self, event):
        try:
            self.tRNA_var.set(mRNA_to_tRNA(self.mRNA_var.get().upper()))
        except KeyError:
            tkinter.messagebox.showerror(title='Error', message='Please ensure you only enter nucleotides')

    def translate_tk(self, event):
        try:
            self.translate_var.set(translate(self.mRNA_var.get().upper()))
        except UnboundLocalError:
            tkinter.messagebox.showerror(title='Error', message='An error has occurred. Please check your '
                                                                'transcribed mRNA and try again.')

    def check_mRNA_tk(self, event):
        try:
            DNA_string = transcribe(self.rand_entry_var.get().upper())
            DNA_template_string = self.mRNA_var.get().upper()
            if DNA_string == DNA_template_string:
                return tkinter.messagebox.showinfo(message='Congrats! You got it!')
            elif len(DNA_string) != len(DNA_template_string):
                return tkinter.messagebox.showerror(message='DNA strands are different lengths.')
            else:
                nucleotides = zip(DNA_string, DNA_template_string)
                incorrect = len([n for n, x in nucleotides if n != x])
                return tkinter.messagebox.showinfo(
                    message=f'You got {incorrect} nucleotide(s) incorrect.\nPlease review.')
        except KeyError:
            tkinter.messagebox.showerror(title='Error', message='Please ensure you only enter nucletodides.')

    def check_tRNA_tk(self, event):
        try:
            DNA_transcribed_string = mRNA_to_tRNA(self.mRNA_var.get().upper())
            mRNA_string = self.tRNA_var.get().upper()
            if DNA_transcribed_string == mRNA_string:
                return tkinter.messagebox.showinfo(message='Congrats! You got it!')
            elif len(DNA_transcribed_string) != len(mRNA_string):
                return tkinter.messagebox.showerror(message='Nucleotide strands are different lengths.')
            else:
                nucleotides = zip(DNA_transcribed_string, mRNA_string)
                incorrect = len([n for n, x in nucleotides if n != x])
                return tkinter.messagebox.showinfo(
                    message=f'You got {incorrect} nucleotide(s) incorrect.\nPlease review.')
        except KeyError:
            tkinter.messagebox.showerror(title='Error', message='Please ensure you only enter nucletodides.')

    def check_translate_tk(self, event):
        peptide_from_mRNA = translate(self.mRNA_var.get().upper()).upper()
        peptide = self.translate_var.get().upper()
        peptide_regex = re.compile(r'(\w{3}-)+(STOP)', re.IGNORECASE)
        mo = peptide_regex.search(peptide)
        if peptide_from_mRNA == peptide:
            return tkinter.messagebox.showinfo(message='Congrats! You got it!')
        elif not mo:
            tkinter.messagebox.showinfo(message='Incorrect format. Please write your answer with the three letter '
                                                'amino acid code followed by a dash, ending with STOP. If there is no '
                                                'protein, please type "No protein found"')
        else:
            tkinter.messagebox.showinfo(message='Incorrect. Please refer back to a codon chart.')

    def __init__(self, parent):
        main_frame = Frame(parent, bg='gainsboro')
        root.title('Transcription and Translation')
        main_frame.pack(fill=BOTH, expand=YES)
        root.option_add('*tearOff', FALSE)
        root.resizable(False, False)

        self.rand_entry_var = StringVar()
        self.mRNA_var = StringVar()
        self.tRNA_var = StringVar()
        self.translate_var = StringVar()
        self.rand_length_var = StringVar()
        self.spin_box_var = StringVar()

        self.welcome_text = Label(main_frame,
                                  text="Welcome to a small program to practice transcription and translation.\n"
                                       "Please see the 'Help' menu for instructions.",
                                  bg='royalblue4', fg='white', font='Times 16 bold')
        self.welcome_text.grid(columnspan=3, row=0, sticky=EW)

        self.rand_text = Label(main_frame,
                               text='Please enter a DNA sequence or calculate a random one. Use the box to your left '
                                    'to input up to a range of 2000',
                               bg='gainsboro')
        self.rand_text.grid(column=1, row=1, rowspan=1, sticky=W)
        self.spin_box_var.set(250)
        self.rand_seq_length = Spinbox(main_frame, width=4, from_=1, to=2000, textvariable=self.spin_box_var)
        self.rand_seq_length.grid(column=0, row=1, sticky=E, pady=5)

        # Entry boxes for user input or input from functions
        self.random_entry = Entry(main_frame, width=100, textvariable=self.rand_entry_var, fg='darkblue')
        self.mRNA_entry = Entry(main_frame, width=100, textvariable=self.mRNA_var, fg='red')
        self.mRNA_to_tRNA_entry = Entry(main_frame, width=100, textvariable=self.tRNA_var, fg='purple')
        self.translate_entry = Entry(main_frame, width=100, textvariable=self.translate_var, fg='darkgreen')

        self.random_entry.grid(column=1, row=3, sticky=EW, padx=5)
        self.mRNA_entry.grid(column=1, row=5, sticky=EW, padx=5)
        self.mRNA_to_tRNA_entry.grid(column=1, row=7, sticky=EW, padx=5)
        self.translate_entry.grid(column=1, row=9, sticky=EW, padx=5)

        # Left side buttons that perform functions
        self.random_button = Button(main_frame, text='Random Sequence', fg='darkblue')
        self.mRNA_button = Button(main_frame, text='mRNA', fg='red')
        self.mRNA_to_tRNA = Button(main_frame, text='tRNA', fg='purple')
        self.translate_button = Button(main_frame, text='Polypeptide Chain', fg='darkgreen')

        self.random_button.grid(column=0, row=3, sticky=EW)
        self.mRNA_button.grid(column=0, row=5, sticky=EW)
        self.mRNA_to_tRNA.grid(column=0, row=7, sticky=EW)
        self.translate_button.grid(column=0, row=9, sticky=EW)

        self.random_button.bind('<ButtonRelease-1>', self.create_rand_seq)
        self.mRNA_button.bind('<ButtonRelease-1>', self.create_mRNA_tk)
        self.mRNA_to_tRNA.bind('<ButtonRelease-1>', self.mRNA_to_tRNA_tk)
        self.translate_button.bind('<ButtonRelease-1>', self.translate_tk)

        # Right side buttons to check user input for accuracy
        self.check_mRNA = Button(main_frame, text='Check', fg='red', padx=10, font='Times 9 bold')
        self.check_tRNA = Button(main_frame, text='Check', fg='purple', padx=10, font='Times 9 bold')
        self.check_translation = Button(main_frame, text='Check', fg='darkgreen', padx=10, font='Times 9 bold')

        self.check_mRNA.grid(column=2, row=5, sticky=EW)
        self.check_tRNA.grid(column=2, row=7, sticky=EW)
        self.check_translation.grid(column=2, row=9, sticky=EW)

        self.check_mRNA.bind('<ButtonRelease-1>', self.check_mRNA_tk)
        self.check_tRNA.bind('<ButtonRelease-1>', self.check_tRNA_tk)
        self.check_translation.bind('<ButtonRelease-1>', self.check_translate_tk)

        # Scrollbars
        self.rand_scrollbar = Scrollbar(main_frame, orient=HORIZONTAL, command=self.random_entry.xview)
        self.mRNA_scrollbar = Scrollbar(main_frame, orient=HORIZONTAL, command=self.mRNA_entry.xview)
        self.mRNA_to_tRNA_scrollbar = Scrollbar(main_frame, orient=HORIZONTAL, command=self.mRNA_to_tRNA_entry.xview)
        self.translate_scrollbar = Scrollbar(main_frame, orient=HORIZONTAL, command=self.translate_entry.xview)

        self.rand_scrollbar.grid(column=1, row=4, sticky=EW, padx=5)
        self.mRNA_scrollbar.grid(column=1, row=6, sticky=EW, padx=5)
        self.mRNA_to_tRNA_scrollbar.grid(column=1, row=8, sticky=EW, padx=5)
        self.translate_scrollbar.grid(column=1, row=10, sticky=EW, padx=5, pady=(0, 50))

        self.random_entry.config(xscrollcommand=self.rand_scrollbar.set)
        self.mRNA_entry.config(xscrollcommand=self.mRNA_scrollbar.set)
        self.mRNA_to_tRNA_entry.config(xscrollcommand=self.mRNA_to_tRNA_scrollbar.set)
        self.translate_entry.config(xscrollcommand=self.translate_scrollbar.set)

        # Making cut/copy/paste active
        self.make_menu(root)
        self.random_entry.bind_class("Entry", "<ButtonRelease-3>", self.show_menu)

        # Main menu and sub-menu's
        main_menu = Menu(root)
        root.config(menu=main_menu)
        sub_menu_file = Menu(main_menu)
        sub_menu_help = Menu(main_menu)

        main_menu.add_cascade(label='File', menu=sub_menu_file)
        sub_menu_file.add_command(label='Clear Inputs', command=self.clear_screen)
        sub_menu_file.add_separator()
        sub_menu_file.add_command(label='Exit', command=root.quit)

        main_menu.add_cascade(label='Help', menu=sub_menu_help)
        sub_menu_help.add_command(label='How to use this program...', command=self.display_how_to)
        sub_menu_help.add_separator()
        sub_menu_help.add_command(label='License', command=self.display_license)


root = Tk()
frame = MyFrame(root)

root.mainloop()
