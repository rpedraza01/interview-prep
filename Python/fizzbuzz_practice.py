#solution 1
# num = input("Please pick a number between 1 and 100 > ")
#  for a number in the range 1 - 100
for num in range(1, 101):
    # if a number is a multiple of 3 AND 5 print "FizzBUzz"
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    # if the first check fails but a number is a multiple of just 3 print "Fizz"
    elif num % 3 == 0:
        print("Fizz")
    # if the second check fails but a number is a multiple of just 5 print "Buzz"
    elif num % 5 == 0:
        print("Buzz")
    # if all checks fail and the number isn't a multiple of 3 and/or 5 just print the number
    else:
        print(num)

# solution 2
# for a number in range 1 - 100
for num in range(1, 101):
    # if a number is a multiple of 15 print "FizzBuzz"
    if num % 15 == 0:
        print("FizzBuzz")
    # if the first check fails but a number is a multiple of 3 print "Fizz"
    elif num % 3 == 0:
        print("Fizz")
    # if the second check fails but a number is a multiple of 5 print "Buzz"
    elif num % 5 == 0:
        print("Buzz")
    # if all checks fail and a number isn't a multiple of 3, 5, or 15 just print the number
    else:
        print(num)

#solution 3
# create the variables a and b and set them to "Fizz" and "Buzz" respectively
a = "Fizz"
b = "Buzz"
# create the variables num1, num2, and num3 and set them to 3, 5, and 15 respectively
num1 = 3
num2 = 5
num3 = 15
# create a for loop with a range of numbers from 1 - 100
for num in range(1, 101):
    # all logic of the for loop is in the print statement
    # print 
    print(a + b if num % num3 == 0 else a if num % num1 == 0 else b if num % num2 == 0 else num)

#solution 4
for(num) in range(1, 101):
    print("Fizz" * (num % 3 == 0) + (num % 5 == 0) * "Buzz" or num)