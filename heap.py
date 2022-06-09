# For max heap se retornar
#  0:  a == b
#  1:  a > b
# -1:  a < b
# if you want a min heap, invert the values
def cmp(a,b) -> int:	
	return 1 if a > b else 0 if a == b else -1 


# definning min-heap
def isheap(H,n): # H = array, i = index of root, n = length of array
	result = True
	for i in range(n//2,-1,-1):
		l = left(i)
		r = right(i)
		largest = i
		if l < len(H) and cmp(H[l], H[i]) > 0:
			largest = l
		if r < len(H) and cmp(H[r], H[largest]) > 0:
			largest = r	
		if largest != i:
			return False
	return result

	
def isheap_naive(H,n):
	for i in range(n):
		l = left(i)
		r = right(i)
		if l < n and not cmp(H[i], H[l]) > -1:
			return False 
		if r < n and not cmp(H[i], H[r]) > -1: 
			return False 
	return True

	
#/*==================================HEAP START====================================*/

def swap(V,a,b):
	V[a],V[b]=V[b],V[a]

#H = heap,i=index
def left(i):
	return 2*i+1
def right(i):
	return 2*i+2
def parent(i):
	return (i-1)//2

def heapify(H,n,i):
	l = left(i)
	r = right(i)
	largest = i
	if l < n and cmp(H[l], H[i]) > 0:
		largest = l
	if r < n and cmp(H[r], H[largest]) > 0:
		largest = r	
	if largest != i:
		swap(H,i,largest)
		heapify(H,n,largest)

def buildheap(H,n):
	for i in range(n//2,-1,-1):
		heapify(H,n,i)

def popheap(H,n):
	z = H[0]
	swap(H,0,n-1)
	heapify(H,n-1,0)
	return z

def bubbleup(H,n,i):
	p = (i-1)//2
	if i < 1:
		return
	if cmp(H[i], H[p]) > 0:
		swap(H,i,p)
		bubbleup(H,n,p)

def insertheap(H,n,a): #-- H=maxheap; n= heapsize; a=element do insert
	#-- supoe-se ter espaço
	# n := n+1
	n = n+1
	H[n-1] = a
	bubbleup(H,n,n-1)
#/*==================================HEAP END====================================*/
