__author__ = 'PoM'


year=int(input())

if (year%5==0 and year%3==0):
    print("FizzBuzz")
elif(year%5==0):
    print("Fizz")
elif(year%3==0):
    print("Buzz")
else:
    print(year)
