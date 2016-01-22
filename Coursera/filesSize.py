import os

total_size = 0
path = 'D:\\Study\\Python\\Automete this boring stuff'
for each_file in os.listdir(path):
	total_size = total_size + os.path.getsize(os.path.join(path, each_file))

print(total_size)
