#magic square is when the row, col and digonal all equal to the same number
#Property of magic square:
#middle number should be 5.
#The number surrounding 5 should be unique and odd
#The number at the corner should unique and even

# arr1 = [1,2,3]
# arr2 = [4,5,6]
# val = zip(arr1,arr2)
# for i,j in val:
#   print(i,j)
def formingMagicSquare(s):
  s = sum(s,[]) #converting 2d into 1d --> [4, 5, 8, 2, 4, 1, 1, 9, 7]
  #There are 8 ways to make a 3×3 magic square
  magic = [[8, 1, 6, 3, 5, 7, 4, 9, 2], [6, 1, 8, 7, 5, 3, 2, 9, 4], [4, 3, 8, 9, 5, 1, 2, 7, 6], [2, 7, 6, 9, 5, 1, 4, 3, 8],  [2, 9, 4, 7, 5, 3, 6, 1, 8], [4, 9, 2, 3, 5, 7, 8, 1, 6], [6, 7, 2, 1, 5, 9, 8, 3, 4], [8, 3, 4, 1, 5, 9, 6, 7, 2]]
  
  minimumCost = 999999
  #need to iterate over each magic square list and compute the difference with our input list
  for magic_list in magic:
    difference = 0
    #zip combines two iterators 
    total_list = zip(s,magic_list)
    for i,j in total_list:
      difference += abs(i-j)
    minimumCost = min(minimumCost,difference)
  return minimumCost


print(formingMagicSquare([[4, 5, 8], [2, 4, 1], [1, 9, 7]]))

