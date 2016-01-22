import webbrowser, sys, pyperclip


ask_address = ''
while ask_address == '':
	print('Enter address: ')
	ask_address = raw_input()
webbrowser.open('https://www.google.com/maps/place/' + ask_address)
	
