#! python3
# mcb.pyw - Multi clipboard programme. Saves and loads pieces of text to the clipboard.
# Usage:
usage_info = """
Usage:
py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
py.exe mcb.pyw delete <keyword> - Deletes keyword and its data.
py.exe mcb.pyw <keyword> - Loads text stored in keyword.
py.exe mcb.pyw list - Loads all keywords to clipboard.
py.exe mcb.pyw clear - Clears all keywords and their data.
"""

import sys, shelve, pyperclip
# Shelve functions
def save_to_shelf(keyword, text):
    mcb_shelf = shelve.open("mcb")
    mcb_shelf[keyword] = text
    mcb_shelf.close()
    print(f"{keyword} successfully saved.")
    
def get_from_shelf(keyword):
    mcb_shelf = shelve.open("mcb")
    if keyword in mcb_shelf:
        pyperclip.copy(mcb_shelf[keyword])
    else:
        mcb_shelf.close()
        print_error_and_exit(f"Error: {keyword} doesn't exist.")
    mcb_shelf.close()
    print(f"{keyword} successfully copied.")
    
def delete_keyword(keyword):
    mcb_shelf = shelve.open("mcb")
    if keyword in mcb_shelf:
        del mcb_shelf[keyword]
        mcb_shelf.close()
    else:
        mcb_shelf.close()
        print_error_and_exit(f"Error: {keyword} doesn't exist.")
    print(f"{keyword} successfully deleted.")
    
def list_all_keywords():
    mcb_shelf = shelve.open("mcb")
    pyperclip.copy(str(list(mcb_shelf.keys())))
    mcb_shelf.close()
    print(f"Full list copied.")
    
def clear_shelf():
    mcb_shelf = shelve.open("mcb")
    mcb_shelf.clear()
    mcb_shelf.close()
    print("Shelf successfully cleared.")

# Error handling    
def print_error_and_exit(error_message):
    print(error_message)
    print(usage_info)
    exit()

# Argument's logic
if len(sys.argv) == 3:
    if sys.argv[1].lower() == "save":
        save_to_shelf(sys.argv[2], pyperclip.paste())
    elif sys.argv[1].lower() == "delete":
        delete_keyword(sys.argv[2])
    else:
        print_error_and_exit(f"Error: {sys.argv[1]} is invalid argument.")
    
elif len(sys.argv) == 2:
    if sys.argv[1] == "list":
        list_all_keywords()
    elif sys.argv[1] == "clear":
        clear_shelf()
    else:
        keyword = sys.argv[1]
        get_from_shelf(keyword)
else:
    print_error_and_exit(f"Error: Invalid number of arguments - {len(sys.argv)} given.")