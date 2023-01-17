def sockMerchant(n, ar):
  sock_count = {}
    
  for sock in ar:
    if sock in sock_count:
      sock_count[sock] += 1
    else:
      sock_count[sock] = 1
    
  count = 0
    
  for sock in sock_count.values():
    count += sock//2
    
  return count