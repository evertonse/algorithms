
from collections import defaultdict
# setting path
from random import randint

randstr = lambda length,ascii=(97,122): ''.join(chr(randint(ascii[0],ascii[1])) for e in range(length))


# For max heap se retornar
#  0:  a == b
#  1:  a > b
# -1:  a < b
# if you want a min heap, invert the values


def compare(a,b) -> int:	
	return 1 if a > b else 0 if a == b else -1 

cmp = lambda a,b: -1 if a.value[0] > b.value[0] else 0 if a.value[0] == b.value[0] else 1

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

class node:
	def __init__(self, value:tuple) -> None:
		self.value 	= 	value
		self.left	=  None
		self.right	=	None
	
	def __repr__(self):
		return f"node->{str(self.value)}"


def freq_count(T, n):
	table = defaultdict(lambda:0)
	for i in range(n):
		table[T[i]] = table[T[i]] + 1 
	return table


def build_trie(table):
	H = []
	n = 0
	for char,freq in table.items():
		H.append( node((freq,char)) )
		n += 1
	buildheap(H,len(H))

	for i in range(n-1):
		x = popheap(H,n); n -=1
		y = popheap(H,n); n -=1

		z = node((x.value[0]+ y.value[0], "*"))
		z.left 	= x
		z.right 	= y
		insertheap(H,n,z); n += 1

	return popheap(H,n)


def build_encoding_table(root:node,code:list,table:dict):
	if root.value[1] != "*":
		table[root.value[1]] = ''.join(code)
		return
	code.append('0')
	build_encoding_table(root.left, code, table)
	code.pop()
	code.append('1')
	build_encoding_table(root.right, code, table)
	code.pop()

def encode(T,n, root):
	
	map = dict()
	build_encoding_table(root,[],map)

	binary_text = [None]*n*8
	for i in range(n):
		binary_text[i] = map[T[i]]

	assert(len(binary_text) == len(T))
	return "".join(binary_text)

def decode(bits,n, root):
	#--vertice v, ficamos trocando pela esquerda ou direita
	v = root 
	decoded_text = [None]*n; 
	i = 0;j = 0
	while i < len(bits):
		if bits[i] == '0':
			v = v.left
		else:
			v = v.right
		
		char = v.value[1]
		if char != "*":
			decoded_text[j] = char
			j = j + 1
			v = root
		i = i + 1
	return "".join(decoded_text)

def programa(T,n):
	table = freq_count(T,n)
	root = build_trie(table)
	
	binary_text = encode(T,n , root)
	print(binary_text)
	
	decoded_text = decode(binary_text,n, root)
	print(decoded_text)

def __main__():
	n = 100
	T = randstr(n,ascii=(97,98))
	T = "Random thing I'm random"; n = len(T)
	programa(T,n)

if __name__ == '__main__':
	__main__()