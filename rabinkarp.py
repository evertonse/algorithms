from distutils.filelist import findall
from utils.stringmatch import randstr, findall

def index(a):
	return ord(a)

def rabinkarp(T,n, P,m):
	matches 	= list[int]()
	q 			= 3354393 		#-- prime number 3354393
	d 			= 64 				#--base d

	dm_1 		= 1				#d^(m-1) = O(m)
	for i in range(m-1):
		dm_1 		= (dm_1*d) % q  
	
	h1 = 0; h2 = 0 
	for i in range(m):
		h1 = (d*h1 + index(P[i])) % q
		h2 = (d*h2 + index(T[i])) % q
	 
	for s in range(0, n-m+1):
		if h1 == h2:
			matches.append(s)
			print(f"shift s {s} works")
		h2 = (d*(h2 - index(T[s])*dm_1) + index(T[s+m])) % q
		# Caso seja negativo
		if h2 <0:
			h2 = h2 + q
	return matches

def __main__():
	n = 1000; m = 8
	P = randstr(m,ascii=(97,98))
	T = randstr(n,ascii=(97,98))
	rabinkarp(T,n, P,m)
		
if __name__ == '__main__':
	__main__()

