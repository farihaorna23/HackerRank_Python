#  1. INTEGER steps
#  2. STRING path
def countingValleys(steps, path):
  step_count = 0
  count_valley = 0
  #go over the string
  #if step is "U" add 1 and step is "D"
  #check if step_count is 0. If 0, check the last step. If "U", then increment count_valley

  for i in range(steps):
    if path[i] == "U":
      step_count += 1
      if step_count == 0:
        count_valley += 1
    elif path[i] == "D":
      step_count -= 1
  return count_valley
    


print(countingValleys(8,"DDUUUUDD"))
print(countingValleys(8,"UDDDUDUU"))
