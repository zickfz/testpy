__author__ = 'PoM'

for i in range(0,101):
    if (i%5==0 and i%3==0):
        print ("FizzBuzz")
    elif (i%5==0):
        print ("Fizz")
    elif (i%3==0):
        print ("Buzz")
    else:
        print (i)
