pidor = 0
semen = '3' * 111
while ('33333' in semen) or ('1111' in semen):
    if '33333' in semen:
        semen = semen.replace('33333', '111', 1)
    else:
        semen = semen.replace('111', '33', 1)
for gey in semen:
    pidor += int(gey)
print(pidor)