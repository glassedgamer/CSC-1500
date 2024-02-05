'''
Problem: Figure out starting temperature and convert it
'''

# Ask if person wants to convert from fahrenheit or celsius
whichOne = input('Would you like to convert from fahrenheit or celsius? (Answer in f or c) ')

# Get input from person for Fareheit degrees
if (fC == 'f'):
  f = int(input('Degrees in Fahrenheit: '))

# Convert Fahrenheit into Celsius
  c = (f - 32) * 5/9

# Display degrees in Celsius
  print('The temperature in Celsius is ', c, 'degrees.')

# Get input from person for Celsius degrees
elif (fC == 'c'):
  c = int(input('Degrees in Celsius: '))

# Convert Celsius into Fahrenheit
  f = (c * 9/5) +32

# Display degrees in Celsius
  print('The temperature in Fahrenheit is ', f, 'degrees.')
