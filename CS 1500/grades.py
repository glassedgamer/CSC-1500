import sys

while(True):
  testScoreList = input('Please enter integers separated by space only:\n')
  numbers = testScoreList.split(' ')

  scoresSum = 0
  try:
    for item in numbers:
      num = float(item)
      
      if((num >= 0) and (num <= 100)):
        scoresSum += num
      else:
        print(item, 'is not between 0 and 100. Try again')
        break
  except:
    print('Value must be number, I quit')
    sys.exit()

  grade = 'No letter grade yet'

  if(not(0 <= num <= 100)):
    print('Test scores must be between 0 and 100. Try again')
    continue
  else:
    average = scoresSum / len(numbers)
    
    if(average < 60.0):
      grade = 'F'
    elif(average < 70.0):
      grade = 'D'
    elif(average < 80.0):
      grade = 'C'
    elif(average < 90.0):
      grade = 'B'
    else:
      grade = 'A'
    print('Your test score average is', f'{average:.1f}', 'and your letter grade is', grade)
