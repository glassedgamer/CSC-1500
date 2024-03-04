import sys

posInt = int(input("Put a positive integer nerd: "))

if(posInt <= 0):
  print('Hey idiot, I said put a positive integer')
  sys.exit()

for i in range(0, posInt):
  if(i % 2 != 0):
    print(i, end=' ')
