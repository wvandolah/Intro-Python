# Write a function is_even that will return true if the passed in number is even.
def is_even(n):
  return (int(n) % 2) == 0
  #   print('even')
  # else:
  #   print('odd')

# Read a number from the keyboard
num = input("Enter a number: ")

# Print out "Even!" if the number is even. Otherwise print "Odd"
if is_even(num):
  print('even')
else:
  print('odd')