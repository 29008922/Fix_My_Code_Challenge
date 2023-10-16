#!/usr/bin/python3

import sys

def fizzbuzz(n):
    ''' '''

    if n < 1 :
        return

    result = []

    for i in range(1, n+1):
        if (i % 3) == 0 and (i % 5) == 0:
            result.append("FizzBuzz")

        elif (i % 3) == 0:
            result.append("Fizz")
        elif (i % 5) == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
        print(" ".json(result))
if __name__ == '__main__' :
    if len(sys.argv) <= 1:
        print("missing number")
        print("usage: ./0-fizzbuzz.py <number>")
        print("Example: ./0-fizzbuzz.py 89")

