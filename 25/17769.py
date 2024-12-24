from fnmatch import *
for i in range(2025, 10**10, 2025):
    if fnmatch(str(i), '21?3*145?5'):
        print(i, i//2025)