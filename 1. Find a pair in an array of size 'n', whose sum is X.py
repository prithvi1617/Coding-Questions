# Python program to check for the sum condition to be satisified 

def hasArrayTwoCandidates(A, arr_size, sum): 
	
	# sort the array 

	A.sort()
	l = 0
	r = arr_size-1
	
	# traverse the array for the two elements 
	while l<r: 
		if (A[l] + A[r] == sum): 
			return 1
		elif (A[l] + A[r] < sum): 
			l += 1
		else: 
			r -= 1
	return 0


# Driver program to test the functions 
A = [1, 4, 45, 6, 10, -8] 
n = 16
if (hasArrayTwoCandidates(A, len(A), n)): 
	print("Array has two elements with the given sum") 
else: 
	print("Array doesn't have two elements with the given sum") 

## This code is contributed by __Devesh Agrawal__ 
