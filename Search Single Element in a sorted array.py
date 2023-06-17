# Python3 program to find the element that
# appears only once

# A Linear Search based function to find
# the element that appears only once

def search(arr, n):
	ans = -1
	for i in range(0, n, 2):
		if (arr[i] != arr[i + 1]):
			ans = arr[i]
			break
	if(arr[n-2] != arr[n-1]):
		ans = arr[n-1]

	# ans = -1 if no such element is present.
	print("The required element is", ans)


# Driver code
arr = [1,1,2,3,3,4,4,8,8]
Len = len(arr)

search(arr, Len)
