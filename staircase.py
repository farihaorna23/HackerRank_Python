def staircase(n):
  j = 1
  for i in range(n-1,-1,-1):
    print(" "*i + "#"*j)
    j += 1

#staircase(4)

def staircase1(n):
  for i in range(1,n+1):
    s = "#"*i
    print(s.rjust(n," "))

staircase1(6)


