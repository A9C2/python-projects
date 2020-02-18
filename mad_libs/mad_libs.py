#! python3
# mad_libs.py - Funny word game.

usage_information = """Usage:
It needs to be run in the same directory where the story file is.
mad_libs.py <filename.txt> - Starts game with specified file. Results are saved in "complete_story.txt" file. 
"""

import sys, os, re
from pathlib import Path

if len(sys.argv) != 2:
    print("Wrong number of arguments")
    print(usage_information)
    exit()

incomplete_story_location = str(Path(sys.path[0]) / sys.argv[1])
if not os.path.exists(incomplete_story_location):
    print(f"Couldn't find story file in {incomplete_story_location}")
    print(usage_information)
    exit()

regex = re.compile(r"ADJECTIVE|NOUN|ADVERB|VERB")
given_words = []

incomplete_story = open(incomplete_story_location, "r")
text = incomplete_story.read()
VOWELS = "AEIOU"
for word in regex.findall(text):
    print(f"Enter {'an ' + word if word[0] in VOWELS else 'a ' + word}") # use "a" or "an"
    given_words.append(input())
incomplete_story.close()

complete_story_location = str(Path(sys.path[0]) / "complete_story.txt")

for i, word in enumerate(regex.findall(text)):
    word_index = text.index(word)
    text_beginning = text[:word_index]
    text_ending = text[word_index + len(word):]
    text = text_beginning + given_words[i] + text_ending
complete_story = open(complete_story_location, "w")
complete_story.write(text)
complete_story.close()