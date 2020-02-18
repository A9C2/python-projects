#! python3
# phone_and_email_extractor.py - Finds phone numbers and email addresses on the clipboard. Copies them to clipboard and print them on screen.
# Usage:
# py phone_and_email_extractor.py

import pyperclip
text = pyperclip.paste()

import re
#phone_number_regex = re.compile(r"\d{3}\.\d{3}\.\d{4}")
email_regex = re.compile(r"\w+@\w+.\w+")

phone_number_regex = re.compile(r"""(
    (\d{3}|\(\d{3}\))?                # US area code (non obligatory when calling person in the same area)
    (\s|-|\.)?                        # Blanc space, hyphen or dot separator
    (\d{3})                           # First 3 digits
    (\s|-|\.)                         # Blanc space, hyphen or dot separator
    (\d{4})                           # Last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # Extension, number in us can be: (206) 333-222 x304
)""", re.VERBOSE)

email_regex = re.compile(r"""(
    [a-zA-Z0-9.!#$%&'*+-/=?^_`{|}~]+    # username
    @                                   # @ symbol
    [a-zA-Z0-9.-]+                      # Domain
    (\.[a-zA-Z]{2,4})                   # dot-something
)""", re.VERBOSE)

matches = []
for groups in phone_number_regex.findall(text):
    phone_number = "-".join([groups[1], groups[3], groups[5]])
    if groups[8] != "":
        phone_number += " x" + groups[8]
    matches.append(phone_number)
for groups in email_regex.findall(text):
    matches.append(groups[0])

# TODO: Copy results to the clipboard
if len(matches) > 0:
    pyperclip.copy("\n".join(matches))
    print("Copied to clipboard.")
    print("\n".join(matches))
else:
    print("No phone numbers or email addresses found.")