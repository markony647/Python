import pyperclip

text = pyperclip.paste()
#print text


# Separate lines and add stars
lines = text.split('\n')
print lines
for i in range(len(lines)):
	lines[i] = '* ' + lines[i]

text = '\n'.join(lines)

pyperclip.copy(text)