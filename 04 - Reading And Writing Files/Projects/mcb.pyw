#! python3 
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard contents to keyword.
#        py.exe mcb.pyw  <keyboard> - Loads keyword contents to clipboard.
#        py.exe mcb.pyw - Loads all keywords to keyboard and displays it.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

#Save Clipboard Content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    #List keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1].lower():
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()