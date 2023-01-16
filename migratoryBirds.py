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

print(migratoryBirds([1,1,2,2,3]))
print(migratoryBirds([1,4,4,4,5,3]))



