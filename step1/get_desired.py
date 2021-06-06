

base = 1
contain7ctr = 0
while contain7ctr != 48:
	num = 7 * base
	base += 1
	if '7' in str(num):
		contain7ctr += 1

print(num)
