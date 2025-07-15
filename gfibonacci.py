def gfibonacci(i):
	a = 0			# First two terms of the sucession
	b = 1
	if i == 1:
		return a	# Avoid entering loop
	elif i == 2:
		return b	# Avoid entering loop
	else:
		i = i-1
		while i > 0:	# Start Loop
			c = a+b
			a = b
			b = c
			# Debug line: print(c)
			i = i-1	# Control variable
		return a

if __name__ == '__main__':
	import sys
	param = int(sys.argv[1])
	print(" > Calculating " + str(param) + "th term ...")
	print(" > gfibonacci(" + str(param) + ") = " + str(gfibonacci(param)))
    