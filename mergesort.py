
  
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]

def merge(arr:list[int], l, m, r):
	
	n1 = m - l + 1
	n2 = r - m
	L = [None]*n1
	R = [None]*n2

	#Copy data to temp arrays L[] and R[] */
	for i in range(n1):
		L[i] = arr[l + i]
	for j in range(n2):
		R[j] = arr[m + 1 + j]

	i, j, k = (0,0,0)
	while i < n1 and j < n2: 
		if (L[i] <= R[j]):
			arr[k] = L[i]
			i+=1
		else:
			arr[k] = R[j]
			j+=1
		k+=1

	while (i < n1): 
		arr[k] = L[i]
		i+=1
		k+=1

	while (j < n2):
		arr[k] = R[j]
		j+=1
		k+=1
  
  

def mergesort(arr:list[int],l:int, r:int ):
	if (l < r): 
		#// Same as (l+r)/2, but avoids overflow for
		#// large l and h
		m = l + (r - l) / 2

		#Sort first and second halves
		mergesort(arr, l, m)
		mergesort(arr, m + 1, r)
		merge(arr, l, m, r)