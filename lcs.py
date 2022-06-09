from utils.Array import Array
from utils.perfomance import measure
from utils.stringmatch import randstr
from array import array

# lcs := longest_common_subsequence 
def lcs(
	T:str, n:int,
	P:str, m:int) -> tuple[int, str, dict]:
	LCS = dict()

	for i in range(n+1):
		LCS[i,0] = 0; 
	for j in range(m+1):
		LCS[0,j] = 0; 
	
	for i in range(1, n+1):
		for j in range(1, m+1):
			if T[i-1] == P[j-1]:
				LCS[i,j] = 1 + LCS[i-1, j-1]  
			else: 
				LCS[i,j]  = max(LCS[i, j-1], LCS[i-1, j]  )


	lenght = max(m,n)
	chars = [None]*lenght
	i=n; j=m; k=lenght -1
	while i > 0 and j > 0:
		if T[i-1] == P[j-1]:
			chars[k] = T[i-1]
			i = i - 1
			j = j - 1
			k = k - 1
		elif LCS[i-1,j] > LCS[i,j-1]:
			i = i - 1
		else:
			j = j - 1

	return LCS[n,m],"".join([str(i) for i in filter(None,chars)]),LCS

def lcs_find(LCS:dict,T,i, P,j):
	if i == 0 or j == 0: # Base case 
		return ""
	# Diminui os dois
	elif T[i-1] == P[j-1]: 
		return lcs_find(LCS, T,i-1, P,j-1) + T[i-1]
	# Diminui apenas o maior entre (i-1, j) e (i, j-1) dessa matriz, 
	# pois só nos interessa a maior subsequencia
	elif LCS[i-1,j] > LCS[i,j-1]:
		return lcs_find(LCS, T,i-1, P,j)
	else: 
		return lcs_find(LCS, T,i, P,j-1)
		
def lcs_print(LCS:dict,T,i, P,j):
	if i == 0 or j == 0: # Base case 
		return
	# Diminui os dois
	elif T[i-1] == P[j-1]: 
		lcs_print(LCS, T,i-1, P,j-1)
		print(T[i-1], end="")
	# Diminui apenas o maior entre (i-1, j) e (i, j-1) dessa matriz, 
	# pois só nos interessa a maior subsequencia
	elif LCS[i-1,j] > LCS[i,j-1]:
		lcs_print(LCS, T,i-1, P,j)
	else: 
		lcs_print(LCS, T,i, P,j-1)
		

#/*======================================================================*/


def test1():
	T = "AGGTAB"
	n = len(T)
	
	P = "GXTXAYB"
	m = len(P)
	num,chars,LCS = lcs(T,n, P,m)
	print(chars)
	string = lcs_find(LCS, T,n, P,m)
	print(f'subsequence = {string}')
	assert(len(chars)==num)

def test():
	n = 200;  T = randstr(n,(97,122))
	m = 200;	P = randstr(m,(97,122))
	
	print(f'T = {T}')
	print(f'P = {P}')
	num, subsequence, LCS  = lcs(T,n, P,m)
	string = lcs_print(LCS, T,n, P,m)
	print(f'subsequence = {subsequence}')
	print(f'subsequence by lcs_find= {string}')
	assert(len(subsequence)==num)


def __main__():
	test1()
	test()


		
if __name__ == '__main__':
	__main__()

