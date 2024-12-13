a = 0
for i in range(8):
  b = int(input())
  if b % 3 == 0 and b % 10 == 4:
    a += 1
print(a)