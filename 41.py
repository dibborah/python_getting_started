# Working with Directores

from pathlib import Path

# Path() # not passing an arguement it will refer the current directory 

# Absolute path: root
# Relative path: with reference to a directly or current directly

# path = Path('emails')
path = Path()
# print(path.exists())
# print(path.mkdir()) # Creates a new directory # But returns nothing
# print(path.rmdir()) # removes a directory # But returns nothing


# for file in path.glob('*.py'): # glob we can search for files using a pattern
for file in path.glob('*'): # '*' -> searches all files and directories (not just .py) 
    print(file)