import lcs as lcs
from utils.stringmatch import randstr

def lcs_from_ed(A,n, B,m):
	ED = dict()
	for i in range(n+1):
		ED[i,0] = i
	for j in range(m+1):
		ED[0,j] = j
	
	for i in range(1,n+1):
		for j in range(1,m+1):
			delete_case = 1 + ED[i-1, j]
			insert_case = 1 + ED[i, j-1]
			# -- são iguais, custa nada
			if A[i-1] == B[j-1]:
				replace_case = ED[i-1, j-1]
			# -- são diferentes replace custa 2
			else:
				replace_case = 2 + ED[i-1, j-1]
			ED[i, j] = min( insert_case, delete_case, replace_case)
	return (n+m - ED[n,m])/2,ED


def lcs_find(ED:dict,A,i, B,j):
	if i == 0 or j == 0: # Base case 
		return ""
	# Diminui os dois
	elif A[i-1] == B[j-1]: 
		return lcs_find(ED, A,i-1, B,j-1) + A[i-1]
	# Diminui apenas o maior entre (i-1, j) e (i, j-1) dessa matriz, 
	# pois só nos interessa a maior subsequencia
	elif (i-1 +j - ED[i-1,j])/2 > (i+j-1 - ED[i,j-1])/2:
		return lcs_find(ED, A,i-1, B,j)
	else: 
		return lcs_find(ED, A,i, B,j-1)
		
def test(A,B):
	n = len(A); m = len(B)
	
	e1,ED 	= lcs_from_ed(A,n,B,m)
	e2,_,LCS = lcs.lcs(A,n,B,m)
	assert(int(e1) == int(e2) )
	
	# for key in ED:
	# 	ED[key] = (n+m - ED[n,m])/2
	string1 = lcs_find(ED,A,n,B,m)
	string2 = lcs.lcs_find(LCS,A,n,B,m)
	
	print(string2)
	print(string1)
	
	assert(len(string1) == e1 )
	assert(len(string2) == e1 )
	assert(string1 == string2)
	
	print(e1)
	print(e2)

def __main__():
	for i in range(100,112):
		A = randstr(i)
		B = randstr(i+20)
		test(A,B)

if __name__ == '__main__':
	__main__()