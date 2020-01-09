# print "Fizz" for numbers that are multiples of 3
# print "Buzz" for numbers that are multiples of 5
# print "FizzBuzz" for numbers that are multiples of 3 AND 5
# put the logic inside of a function
# call the inside of a while True loop
# end the while True loop with an exit string so that the user can pick another number

def number(user_num):
	if user_num % 15 == 0:
		print('FizzBuzz, your number is a multiple of 3 and 5')
	elif user_num % 3 == 0:
		print('Fizz, your number is a multiple of 3')
	elif user_num % 5 == 0:
		print('Buzz, your number is a multiple of 5')
	else:
		print(f'{user_num} is not a multiple of 3 and/or 5')

while True:
	num = int(input('Please pick a number and I\'ll check if it is a multiple of 3 and/or 5 > '))
	number(num)
	exit = input('Would you like to pick another number? > ')
	if exit != 'yes':
		break
