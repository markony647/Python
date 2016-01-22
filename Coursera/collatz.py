result = 0
def collatz(number):
	global result
	if number % 2 == 0:
		print('The number is even')
		result = number // 2
		print result
		return result
	elif number % 2 == 1:
		print('The number is odd')
		result = 3 * number + 1
		print result
		return result



user_input = int(raw_input('Enter any integer pls: '))
global result
while result != 1:
	collatz(user_input)
	user_input = result




