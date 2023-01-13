def birthday(s, d, m):
  i = 0
  j = m
  count = 0
  stop = len(s) + 1

  while j != stop:
    arr = s[i:j]
    if sum(arr) == d:
      count += 1
    i+=1
    j+=1
  return count


print(birthday([4],4,1))
