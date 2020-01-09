# print "Fizz" for numbers that are multiples of 3
# print "Buzz" for numbers that are multiples of 5
# print "FizzBuzz" for numbers that are multiples of 3 AND 5

# for num in range(1, 1001):
# 	if num % 3 == 0 and num % 5 == 0:
# 	# if num % 15 == 0:
# 		print("FizzBuzz")
# 	elif num % 3 == 0:
# 		print("Fizz")
# 	elif num % 5 == 0:
# 		print("Buzz")
# 	else:
# 		print(f'{num} is not a multiple of 3 and/or 5')

num = int(input('Please pick a number > '))
if num % 15 == 0:
	print("FizzBuzz, your number is a multiple of 3 and 5")
elif num % 3 == 0:
	print("Fizz, your number is a multiple of 3")
elif num % 5 == 0:
	print("Buzz, your number is a multiple of 5")
else:
	print(f'{num} is not a multiple of 3 and/or 5')