
# se retornar
# 0:  a == b
# 1:  a > b
# -1: a < b
def cmp(a,b) -> int:
	return 1 if a > b else 0 if a == b else -1 


def is_maxheap(H,n): # H = array, i = index of root, n = length of array
	result = True
	for i in range(n//2,-1,-1):
		l = left(i)
		r = right(i)
		largest = i
		if l < len(H) and H[l] > H[i]:
			largest = l
		if r < len(H) and H[r] > H[largest]:
			largest = r	
		if largest != i:
			return False
	return result

	
def is_maxheap_naive(H,n):
	for i in range(n):
		l = left(i)
		r = right(i)
		if l < n and not H[i]>=H[l]:
			return False 
		if r < n and not H[i]>=H[r]: 
			return False 
	return True

	
#/*==================================START====================================*/

def swap(V,a,b):
	V[a],V[b]=V[b],V[a]

#H = heap,i=index
def left(i):
	return 2*i+1
def right(i):
	return 2*i+2
def parent(i):
	return (i-1)//2

def max_heapify(H,n,i):
	l = left(i)
	r = right(i)
	largest = i
	if l < n and H[l] > H[i]:
		largest = l
	if r < n and H[r] > H[largest]:
		largest = r	
	if largest != i:
		swap(H,i,largest)
		max_heapify(H,n,largest)

def build_max_heap(H,n):
	for i in range(n//2,-1,-1):
		max_heapify(H,n,i)

def remove_root(H,n):
	z = H[0]
	swap(H,0,n-1)
	max_heapify(H,n-1,0)
	return z

def bubbleup(H,n,i):
	p = (i-1)//2
	if i < 1:
		return
	if H[i] > H[p]:
		swap(H,i,p)
		bubbleup(H,n,p)

def insert_maxheap(H,n,a): #-- H=maxheap; n= heapsize; a=element do insert
	#-- supoe-se ter espaço
	# n := n+1
	n = n+1

	H[n-1] = a
	bubbleup(H,n,n-1)
#/*==================================END====================================*/
