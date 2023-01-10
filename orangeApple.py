def countApplesAndOranges(s, t, a, b, apples, oranges):
  appleCount = 0
  ornageCount = 0

  #go over the apple and oranges array
  # get the sum 
  # and check if the sum falls in between s and t -> if yes, increment appleCount
  for apple in apples:
    distance = a + apple
    if distance >= s and distance <= t:
      appleCount += 1
  
  for orange in oranges:
    distance = b + orange
    if distance >= s and distance <= t:
      ornageCount += 1
  
  print(f"{appleCount}\n"
        f"{ornageCount}")

countApplesAndOranges(7,11,5,15,[-2,2,1],[5,-6])
