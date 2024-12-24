from fnmatch import *
for i in range(98591, 10**10, 98591):
    if fnmatch(str(i), '5?2*3?3?'):
        print(i, i//98591)