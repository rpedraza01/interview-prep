# print "Fizz" for numbers that are multiples of 3
# print "Buzz" for numbers that are multiples of 5
# print "FizzBuzz" for numbers that are multiples of 3 AND 5
# put the logic inside of a function
# call the inside of a while True loop
# end the while True loop with an exit string so that the user can pick another number

import random

# I would like to combine the 2 functions into one that checks the number choice of both the user and computer
def fb_user_number(user_num_choice):
	if user_num_choice % 15 == 0:
		print('FizzBuzz, your number is a multiple of 3 and 5')
	elif user_num_choice % 3 == 0:
		print('Fizz, your number is a multiple of 3')
	elif user_num_choice % 5 == 0:
		print('Buzz, your number is a multiple of 5')
	else:
		print(f'Your number, {user_num_choice}, is not a multiple of 3 and/or 5')

def fb_cpu_number(cpu_num_choice):
	if cpu_num_choice % 15 == 0:
		print('FizzBuzz, the computer\'s number is a multiple of 3 and 5')
	elif cpu_num_choice % 3 == 0:
		print('Fizz, the computer\'s number is a multiple of 3')
	elif cpu_num_choice % 5 == 0:
		print('Buzz, the computer\'s number is a multiple of 5')
	else:
		print(f'The computer\'s number, {cpu_num_choice}, is not a multiple of 3 and/or 5')

while True:
	users_num = int(input('Please pick a number and I\'ll check if it is a multiple of 3 and/or 5. The computer will also be picking a number. > '))
	cpus_num = random.choice(range(1, 100001))
	# not sure how to get the below commented out code to allow the computer to make a random choice without specifying a range
	# I want the computer to be free to make any number choice just like the user
	# cpus_num = random.randint()
	print(f'The computer picked {cpus_num}')
	fb_user_number(users_num)
	fb_cpu_number(cpus_num)
	exit = input('Would you like to pick another number? > ')
	if exit != 'yes':
		break