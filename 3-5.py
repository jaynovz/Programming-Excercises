__author__ = 'Jessica'

import random
a = random.randrange(0,10)
b = random.randrange(0,10)
c = random.randrange(0,10)
print a
print b
print c

while True:
	d = int(raw_input('What is the sum?'))
	if d == a + b + c:
		print "True"
		break
	else:
		print "False"