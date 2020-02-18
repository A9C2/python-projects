#! python3
# regex_search.py - a programme that opens all .txt files in a folder and searches for any line that matche's user-supplied regular expression.
# Usage:
# py regex_search.py <user_defined_regex> - Search for any regex matches in .txt files in current directory and print them to screen.
import sys, os, re
os.chdir(sys.path[0])

if len(sys.argv) != 2:
    print("Wrong number of arguments.")
    exit()

text_file_regex = re.compile(r"[^\|]*\.txt")
user_regex = re.compile(sys.argv[1])
print(f"Used regex: {sys.argv[1]}")

for file_name in text_file_regex.findall("|".join(os.listdir())):
    f = open(file_name, "r")
    text = f.read()
    if len(user_regex.findall(text)) == 0:
        print(f"Nothing found in {file_name}")
    else:
        num_of_matches = len(user_regex.findall(text))
        for match in user_regex.findall(text):
            print(f"{num_of_matches} {'match' if num_of_matches == 1 else 'matches'} found in {file_name}")
            print(match)
    f.close()

