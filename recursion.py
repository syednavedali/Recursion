import argparse

def factorial(n):
  if n==0:
   return 1
  elif n < 0:
    return 0
  else:
    return n * factorial(n-1)

parser = argparse.ArgumentParser()
parser.add_argument('argument', type=int)
input_argument = parser.parse_args().argument

print(factorial(input_argument))