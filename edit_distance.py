def ed(A,n, B,m):
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
			# -- são diferentes replace custa 1
			else:
				replace_case = 1 + ED[i-1, j-1]
			ED[i, j] = min( insert_case, delete_case, replace_case)
	return ED[n,m]


def __main__():
	A = "ABCD" ; n = len(A)
	B = "AECDB" ; m = len(B)
	e = ed(A,n,B,m)
	print(e)

if __name__ == '__main__':
	__main__()