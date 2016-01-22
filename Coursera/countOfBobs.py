bob_number = 0
step = 0

while step <= len(s):
    if s[0 + step :3 + step] == 'bob':
        bob_number += 1
        step += 1
    else:
        step += 1
print 'Number of times bob occurs is: ' + str(bob_number)