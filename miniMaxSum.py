def miniMaxSum(arr):
  prev_value = 0
  all_sum = []

  for i in range(len(arr)):
    if i > 0:
      prev_value += arr[i-1]
    
    split_arr = arr[i+1:]
    split_arr.append(prev_value)
    all_sum.append(sum(split_arr))
  
  max_value = max(all_sum)
  min_value = min(all_sum)

  print(min_value,max_value)

miniMaxSum([1,2,3,4,5])

def miniMaxSum1(arr):
  # [3,1,5,2,4]
  #[1,2,3,4,5] -> ignore 1 sum([2,3,4,5]) --> max value
  #[1,2,3,4] -> ignore 5 sum([1,2,3,4]) -> min value
  sort = sorted(arr)

  print(sum(sort[:-1]), sum(sort[1:]))

miniMaxSum1([3,1,5,2,4])

