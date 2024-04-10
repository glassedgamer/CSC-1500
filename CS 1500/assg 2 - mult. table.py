'''
  This program generates a multiplication table based on user inputs. One
  input will be for what number is getting multiplied, and the other row is
  for how many rows there are. Neither values can be equal to or less than 0,
  nor can they use characters other numbers. If the user enters a number less than
  or ueal to 0, it lets them know and restarts. If they enter a value that uses
  characters other than a number, it lets them know and quits.
'''

# Allows for use of exit() function
import sys 

# Repeatedly ask the user for the table value and amount of rows, and prints table
while(True):
  # Asks user for table value and amount of rows
  tableVal = input('What value would you like to see a table for? ')
  rowVal = input('How many rows would you like? ')

  # If either of user inputs are >= 0, then multiply row & table values and print line
  # Also checks if user input is a number, and quits if not
  try:
    if((int(rowVal) > 0) and (int(tableVal) > 0)):
      for row in range(1, int(rowVal) + 1):
        product = int(tableVal) * int(row)
        print(tableVal, 'x', row, '=', product)
    else:
      print('Neither of your values can be less than or equal to 0')
      continue
  except:
      print('One or both of your values has non-numeric values, so quitting')
      sys.exit()
