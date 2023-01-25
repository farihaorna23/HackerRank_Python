def lengthOfLongestSubstring(s):
  #check if string is valid or not
  if s == "":
    return 0
  
  i = 0
  j = 0
  max_value = 0
  length = len(s)
  set_list = []
  while(i < length):
    current_val = s[i]
    while(current_val in set_list):
      set_list.remove(s[j])
      j+=1
    set_list.append(current_val)
    max_value = max(max_value, i - j + 1)
    i+=1
  return max_value
    

print(lengthOfLongestSubstring("pwwkew"))

