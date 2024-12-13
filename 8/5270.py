s = sorted('МФБРАХИЙ')
# АМФИБРАХИЙ
c = 0
from time import process_time
for a1 in s:
    for a2 in s:
        for a3 in s:
            for a4 in s:
                for a5 in s:
                    for a6 in s:
                        for a7 in s:
                            for a8 in s:
                                for a9 in s:
                                    for a10 in s:
                                        a = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10
                                        if ('АА' in a) or ('ИИ' in a) or ('АИ' in a) or ('ИА' in a):
                                            c += 1
print(c, process_time())