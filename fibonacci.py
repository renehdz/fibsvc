# -*- coding: utf-8 -*-
"""
    fibonacci
    -----------------
    Computes Fibonacci sequences
"""


def fibonacci_sequence(n):
  """Returns a list of n Fibonacci numbers."""
  result = []
  a, b = 0, 1
  for i in range(n):
    result.append(a)
    a, b = b, a+b
  return result


def try_parse_positive_int(n):    
  try:
    parsed_int = int(n)
    is_positive = parsed_int >= 0
    return is_positive, parsed_int
  except ValueError:    
    return False, 0


def main():
  while True:
    raw = raw_input("Fibonacci: ")

    if raw.strip() == "exit":
        break

    valid_input, n = try_parse_positive_int(raw)
    if not valid_input:
      print "%s is not a positive integer" % (raw)
    else:
      print fibonacci_sequence(n)


if __name__ == "__main__": main()
