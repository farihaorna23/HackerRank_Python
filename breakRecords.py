def breakingRecords(scores):
  minimum = scores[0]
  maximum = scores[0]
  minCount = 0
  maxCount = 0

  for i in range(1,len(scores)):
    if scores[i] < minimum:
      minimum = scores[i]
      minCount += 1
    elif scores[i] > maximum:
      maximum = scores[i]
      maxCount += 1
  
  return [maxCount, minCount]


print(breakingRecords([3,4,21,36,10,28,35,5,24,42]))