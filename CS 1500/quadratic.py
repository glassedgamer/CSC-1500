"""
Problem: Solve quadratic equation ax^2 + bx + c
"""
import sys
import math

# Ask user for inputs a, b, c, and store them
a = int(input('Please enter the value for a: '))
b = int(input('Please enter the value for b: '))
c = int(input('Please enter the value for c: '))

# Verify if a is not equal to zero, output message otherwise
if(a == 0):
  print('a cannot be 0, you idiot. Time to quit.')
  sys.exit()

# Compute the discriminant b^2-4ac and store it as d
d = b * b - (4*a*c)
print(d, 'is the discriminant.')

# if d < 0, output no solution
if(d < 0):
  print('d cannot be 0 you idiot, there is no solution. I quit')
  sys.exit()

# else if d = 0, compute and print the unique solution -b/2a
elif(d == 0):
  print('The unique solution is ', -b/2*a)

# else compute and display both the solutions
else:
  neg_x = (-b - math.sqrt(d)) / (2*a)
  pos_x = (-b + math.sqrt(d)) / (2*a)

  print('Your answers are ', pos_x, ' and ', neg_x)
