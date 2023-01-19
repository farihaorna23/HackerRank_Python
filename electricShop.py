def getMoneySpent(keyboards, drives, b):
    max_expensive = 0
    #nested loops
    #make sure we don't consider any value that is above or equal to the budget
    #the sum of max_expensive should be less than or equal to budget
    for keyboard in keyboards:
      if keyboard < b:
        for drive in drives:
          if drive < b:
            total = keyboard + drive
            if total <= b and total > max_expensive:
              max_expensive = total
    
    if max_expensive == 0:
      return -1
    else:
      return max_expensive

print(getMoneySpent([4],[5],5))
print(getMoneySpent([40,50,60],[5,8,12],60))
print(getMoneySpent([3,1],[5,2,8],10))

