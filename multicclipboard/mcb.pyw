#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: mcb save <keyword> - Saves clipboard to keyword
#        mcb <keyword> - Loads keyword to clipboard.
#        mcb list - Loads all keywords to clipboard.
#        mcb delete <keyword> - Delete the save for the keyword.

import shelve,pyperclip,sys

mcbShelf = shelve.open('mcb')

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()

elif len(sys.argv) == 2:
    #List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

# TODO: Delete content
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcbShelf[sys.argv[2]]

mcbShelf.close()
