#! python3
# date_detection.py Detects dates in DD/MM/YYYY format on clipboard. Prints found matches and checks dates validity.
#import sys

def is_valid_date(day, month, year):
    MONTHS_LENGTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_num = int(day)
    month_num = int(month)
    year_num = int(year)
    
    month_length = MONTHS_LENGTHS[month_num - 1]
    
    # February
    if month_num == 2 and day_num - 1 == month_length:
        if year_num % 100 == 0 and not year_num % 400 == 0:
            return False
        if year_num % 4 == 0:
            return True
    # Every other month
    if day_num > month_length:
        return False
    return True

import pyperclip
text = pyperclip.paste()

import re
date_regex = re.compile("""(
    ([0][1-9]|[1-2][0-9]|[3][01])
    /
    ([0][1-9]|[1][0-2])
    /
    (\d{4})
)""", re.VERBOSE)

matches = []
validity = []
for groups in date_regex.findall(text):
    matches.append(groups[0])
    day = groups[1]
    month = groups[2]
    year = groups[3]
    validity.append(is_valid_date(day, month, year))

if len(matches) > 0:
    pyperclip.copy("\n".join(matches))
    print("Copied to clipboard.")
    print("\n".join(matches))
    print("\nChecking date validity...")
    for i in range(len(matches)):
        if validity[i]:
            print(matches[i] + " is a valid date.")
        else:
            print(matches[i] + " is not a valid date.")
else:
    print("No dates found. Press enter to exit.")