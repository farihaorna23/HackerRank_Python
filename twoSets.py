# returns the number of items that satifisfies two condition
#multiples of first array
#muliples of 2 and 6
#factor of second array
#factor of 24 and 36. EX- 24/2 -> 12 (12 and 2 are factor of 24)

#brute force approach will be to get multiples of 2 and 6
#and then get all the factors of 24 and 36
#then find all the integers that are present in all 4 list and return the count

#efficient approach
#get only the integers that both 2 and 6 have in common --> 6,12,18,24
#get common factor of 24,36 -> 2,3,4,6,12,
def getTotalX(a, b):
  #get mutiples of all the integers of a
  #get factorial of all the integers of b
  multiple = []
  factorial = []
  count = 0
  total_length = len(a+b) #4 all potential integers needs to appear 4 times
  for i in range(1,101):
    for num in a:
      if i % num == 0:
        multiple.append(i)
    
    for num in b:
      if num % i == 0:
        factorial.append(i)
  
  both_list = multiple + factorial
  possible_integers = []
  for num in both_list:
    if both_list.count(num) == total_length:
      count += 1
    
  return count//total_length



# print(getTotalX([2,6], [24,36]))
print(getTotalX([2,4],[16,32,96]))

