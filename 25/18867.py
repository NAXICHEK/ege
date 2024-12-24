from fnmatch import *
for i in range(2025, 10**10, 2025):
    if fnmatch(str(i), '33?2*42?') and fnmatch(str(i), '*32??2?') and i % 2025 == 0:
        print(i, i//2025)