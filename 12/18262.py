for i in range(1000):
    a = 0
    s = '>' + '0'*17 + '3'*i + '2'*17
    while '>3' in s or '>2' in s or '>0' in s:
        if '>3' in s: s = s.replace('>3', '22>', 1)
        if '>2' in s: s = s.replace('>2', '2>', 1)
        if '>0' in s: s = s.replace('>0', '3>', 1)
    s = s.replace('>', '')
    for f in s:
        a += int(f)
    if a % a**0.5 == 0 and a / a**0.5 == float(a**0.5):
        print(i)