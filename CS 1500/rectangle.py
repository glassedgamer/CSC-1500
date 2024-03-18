'''
Problem: ask user for length and width (as positive numbers), compute the
area and perimeter and display
'''

import sys

# Ask for length from user and store in variables
length = float(input('Length of rectangle: '))
width = float(input('Width of rectangle: '))

# Check if length is negative, and quits if so
if (length < 0):
  print('Length cannot be negative')
  sys.exit()

# Check if width is negative, and quits if so

elif (width < 0):
  print('Width cannot be negative')
  sys.exit()

else:

# Compute area and perimeter and store them in variables
  area = length * width
  perimeter = (length * 2) + (width * 2)

# Display values
  print('The area is', f'{area:.2f}', 'and the perimeter is', f'{perimeter:.2f}')
