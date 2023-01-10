# Grading Students
def gradingStudents(grades):
  result = []
  for grade in grades:
      # get next_multiple 
      next_multiple = 5 * ((grade//5)+1)
      # if next_multiple differnce with grade is less than 3, round to next mutiple
      if next_multiple - grade < 3 and next_multiple >= 40:
        result.append(next_multiple)
      else: #else don't round
        result.append(grade)
  
  return result

print(gradingStudents([73,67,38,33]))

