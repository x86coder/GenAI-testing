def gbubblesort(list):
	for k in range(0, len(list)):			# Repeat k times. With k being the length of the list.
		# Debug line print(" ** RUN")
		for i in range(1, len(list)):		# For loop compares element by element. Start with the second element on the list first
			#print(" ** cmp " + str(list[i]) + " & " + str(list[i-1]))
			if list[i] < list[i-1]:			# If element to the right is lower, then switch positions:
				#print(" ** xchg")
				aux = list[i-1]
				list[i-1] = list[i]
				list[i] = aux
				#Debug line print(list)
	return list

if __name__ == '__main__':
	print("gbubblesort(x) - Usage: python gbubblesort.py 20,10,3,4,2")
	import sys
	params = sys.argv[1].split(',')
	print(" > Sorting " + str(params) + " ...")
	
	# Convert strings into numbers
	numbers = []
	for n in range(0, len(params)):
		numbers.append(int(params[n]))
		
	# Call main function
	print(" > Result:")
	print(gbubblesort(numbers))
    