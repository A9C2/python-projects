#! python3
# mad_libs.py - Funny word game.
# Usage:
# mad_libs.py <filename_with_extension> - Starts game with specified file. Results are saven in "complete_story.txt" file

import sys, os, re
from pathlib import Path

if len(sys.argv) != 2:
    print("error")
    exit()

incomplete_story_location = str(Path(sys.path[0]) / sys.argv[1])
if not os.path.exists(incomplete_story_location):
    print("error")
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