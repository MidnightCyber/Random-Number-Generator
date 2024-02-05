def exit():
  import sys
  sys.exit()
def is_an_integer(s):
  try:
    int(s)
    return True
  except ValueError:
    return False

def get_int(prompt):
  i = input(prompt)
  while i == "Exit":
    exit()
  while i == "Feedback":
    print()
    feed = input('What is your feedback?\n')
    print()
    email =  input('What is your email? We will use this only to respond to you.\n')
    try:
      with open('feedback.txt', 'a') as feedback:
        feedback.write(feed + '\n' + 'Email:' + email + '\n' + '\n')
        print()
        print('Thank you for your feedback! We will take a look at it.')
        print()
    except Exception:
      print('Something went wrong')
    i = input(prompt)
  while not is_an_integer(i):
    i = input(
        f'You have entered "{i}".' +
        f' "{i}" is not an integer. Please enter an integer:\n')
  return int(i)

def random_gen():
  import random

  number1 = get_int('Choose your first number.\n')
  print()
  number2 = get_int('Choose your second number.\n')
  print()
  if number1 > number2:
    print('Your random number is', random.randint(number2, number1))
    print()
  if number1 < number2:
    print('Your random number is', random.randint(number1, number2))
    print()
  if number1 == number2:
    print('Your numbers are the same, please try again')
    print()
    random_gen()
  if number1 == 69 and number2 == 420:
    print('Did you have to do that?')
    print()
  if number1 == 420 and number2 == 69:
    print('Did you have to do that?')
    print()
while True:
  random_gen()
