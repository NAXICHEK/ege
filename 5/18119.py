h = []
def cc(x, base):
	s = ''
	while x > 0:
		s = str(x % base) + s
		x = x // base
	return s
for i in range(1, 100):
    a = cc(i, 3)
    if sum(map(int, a)) % 2 == 0:
        a = '1' + a + '2'
    else:
        a = '2' + a + '0'
    b = int(a, 3)
    h.append(b)
for num in sorted(h):
    if num > 100:
        print(num) # 113
        break
print(sorted(h)) # 113
print(h)