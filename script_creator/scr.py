import sys
from pathlib import Path
if len(sys.argv) not in [2, 3]: # If no argument or too many arguments are given
    print("""Error: wrong number of arguments
    Usage: scr [filename] [optional_suffix]
    [filename] - base name of the file
    [optional_suffix] - without dot, default "py"
    """)
    sys.exit()

file_location = str(Path(sys.path[0]) / Path("Working") / sys.argv[1]) # Newly created file's path without extension

import os
suffix = ".py"
if len(sys.argv) == 3:
    suffix = "." + sys.argv[2]
    
if (os.path.exists(file_location + suffix)):
    print("Python file already exists in Working directory.")
    print(file_location)
    print("Terminating program...")
    sys.exit()
if (os.path.exists(file_location + ".bat")):
    print("Batch file already exists in Working directory.")
    print(file_location)
    print("Terminating program...")
    sys.exit()

py_file = open(file_location + suffix, "w")
py_file.write(f"#! python3\n# {sys.argv[1] + suffix} - ")
py_file.close()

batch_file = open(file_location + ".bat", "w")
batch_file.write(f'@py.exe "{file_location + suffix}" %*\n')
batch_file.write("@pause")
batch_file.close()

print(f"Files successfully created in {file_location}")