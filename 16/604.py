def F(n):
   # print(2*n+1)
   if n>1:
      # print(3*n-8)
      F(n-1)
      F(n-4)
print(F(2984) - F(2988))