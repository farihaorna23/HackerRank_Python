def pageCount(n, p):
  front_steps = 0
  back_steps = 0

  # front
  if n % 2 == 0:
    if n == p:
      front_steps += ((n-2)//2)+1
  
  for i in range(2,n,2):
    if 1 == p:
      break
    elif i == p or (i+1) == p:
      front_steps +=1
      break
    elif i != p and (i+1) != p:
      front_steps += 1
  # back
  if n%2 != 0:
    for i in range(n,0,-2):
      if i == p or (i-1) == p:
        break
      elif i != p and (i-1) != p:
        back_steps += 1
  else:
    back_steps += 1
    for i in range(n-1,0,-2):
      if n == p:
        back_steps = 0
        break
      if i == p or (i-1) == p:
        break
      elif i != p and (i-1) != p:
        back_steps += 1
  return min(front_steps,back_steps)

print(pageCount(4,4))
        


