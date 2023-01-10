# intersecting point
# a1 + nd1= a2 + nd2
# a1 - a2 = nd2 - nd1
# a1 - a2 = n(d2 - d1) --> now divide (d2 - d1) to isolate n.
# (a1-a2)/(d2-d1) = n

# So, here we can find some REAL number n that would satisfy the equation given the conditions 

# a1<a2 AND d1<d2 evaluates to false. 

# so long as this is true, n exists as an answer. However, we want n to be a postive whole number in this problem. This is why mod % is used. It takes the division:

# (a1-a2)/(d2-d1) and seeks a natural number where no remainder exists, i.e evaluates to n = integer remainder 0

#speed= distance * time
#distance = speed / time(jump)

#the second kangaroo condition is always ahead of the first kangaroo, 
#so if its jump rate is also higher or euqal, kangaroo 1 can never catch up
def kangaroo(x1, v1, x2, v2):
    if v2>=v1:
        return "NO"
    else:
        if (x2-x1) % (v2-v1) == 0:
            return "YES"
        else:
            return "NO"



print(kangaroo(2,1,1,2))
print(kangaroo(0,3,4,2))
print(kangaroo(0,2,5,3))
