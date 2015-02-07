__author__ = 'Jessica'

#qpy:gui
import random
a = random.randrange(1,99)
b = random.randrange(1,99)
print a
print b

c = int(raw_input('What is the sum?'))
# c = 10

#c = raw_input('What is the sum?')
if c == a + b:
	print "True"
else:
	print "False"
