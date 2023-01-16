def migratoryBirds(arr):
  counts = {}
  length = len(arr)
  
  for item in arr:
    if item in counts:
      counts[item] += 1
    else:
      counts[item] = 1
  
  max_value = 0
  for count in counts.values():
    if count > max_value:
      max_value = count
  
  duplicates = []

  for value,count in counts.items():
    if count == max_value:
      duplicates.append(value)
  
  if len(duplicates) == 1:
    return duplicates[0]
  else:
    return min(duplicates)

def migratoryBirds1(arr):
  l = [0] * len(arr)

  for i in range(len(arr)):
    l[arr[i]] +=1
    # [0, 2, 2, 1, 0] 
  # index method goes from left to right
  # so in case of duplication, it will return the smallest index
  return l.index(max(l))
  

print(migratoryBirds1([1,1,2,2,3]))
# print(migratoryBirds([1,4,4,4,5,3]))



