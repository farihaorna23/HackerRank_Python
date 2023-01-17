def dayOfProgrammer1(year):
  if year == 1918:
    return ''
  elif year >= 1700 and year <= 1917:
    if year % 4 == 0:
      return "12.09.%s" % year
    else:
      return "13.09.%s" % year
  elif year > 1918:
    if year % 100 == 0 or year % 4 == 0 and year % 100 != 0:
      return "12.09.%s" % year
    else:
      return "13.09.%s" % year

print(dayOfProgrammer1(1800))


def dayOfProgrammer(year):
  months = [31,28,31,30,31,30,31,31,30,31,30,31]
  #for julian calender (1700-1917)
  if year == 1918:
    months[1] = 28-13
  elif year >= 1700 and year <= 1917:
    #check if leap year
    if year % 4 == 0:
      months[1] = 29
  elif year >= 1919:
    # check for leap year
    if year % 400 == 0 or (year%4 == 0 and year % 100 != 0):
      months[1] = 29
  
  sum_value = 0
  i = 0
  difference = 0
  while i < len(months):
    sum_value += months[i]
    difference = 256-sum_value

    if difference < months[i+1]:
      break

    i+=1
  
  month = i+2

  if month < 10:
    month = str(month).zfill(2)
  
  
  return f"{difference}.{month}.{year}"



  





  #for Gregorian calendar (Since 1919)
  #Exceptional case when year is 1918 and 13 days will be cut from februrary