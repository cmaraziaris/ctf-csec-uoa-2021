
from math import floor, sqrt

n = 127670779

base = floor(sqrt(n))

while base > 0:
	if n % base == 0:
		print('p is: ', base)
		print('q is: ', n // base)
		exit(0)

	base -= 2
