#! python3
# mcb.pyw - Save and loads pieces of text to the clipboards
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard
#        py.exe mcb.pyw list - loads all keywords to clipboard
#        py.exe mcb.pyw delete <keyword> - Deletes keyword from shelve
#        py.exe mcb.pyw deleteall - Deletes all keywords from shelve
#        py.exe mcb.pyw printall - Creates a list of all values onto the clipboard
#        py.exe mcb.pyw addto - Creates list of items to add to printall list

import shelve
import pyperclip
import sys


mcb_shelf = shelve.open('mcb')

    # Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcb_shelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcb_shelf[sys.argv[2]]
elif len(sys.argv) == 2:
    # List keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
    elif sys.argv[1].lower() == 'deleteall':
        for keyword in list(mcb_shelf.keys()):
            del mcb_shelf[keyword]
    elif sys.argv[1].lower() == 'printall':
        value_list = []
        for key, value in list(mcb_shelf.items()):
            value = value.strip()
            value_list.append(value)
        pyperclip.copy(str(value_list))
    elif sys.argv[1].lower() == 'addto':
        value_list = []
        value_string = ''
        for key, value in list(mcb_shelf.items()):
            value = value.strip()
            value_list.append(value)
        for item in value_list:
            item = "'%s'," % item
            value_string += item
        pyperclip.copy(value_string)
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])
mcb_shelf.close()
