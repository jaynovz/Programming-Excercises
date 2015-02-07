__author__ = 'Jessica'

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

a = raw_input("Enter a nine digit number:")

while not is_number(a):
            a = raw_input("Enter a nine digit number:")
while len(a) != 9:
            a = raw_input("Enter a nine digit number:")


d1 = int(a[0])
d2 = int(a[1])
d3 = int(a[2])
d4 = int(a[3])
d5 = int(a[4])
d6 = int(a[5])
d7 = int(a[6])
d8 = int(a[7])
d9 = int(a[8])

d0 = (d1 * 1 + d2 * 2 + d3 * 3 + d4 * 4 + d5 * 5 + d6 * 6 + d7 * 7 + d8 * 8 + d9 * 9) % 11
print str(a) + str(d0)
