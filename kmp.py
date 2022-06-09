def lps_table(P,m):
	lps = [None]*(m)
	lps[0] = 0 
	j = 0
	# i for 1 downto m
	for i in range(1,m):
		while j != 0 and P[j] != P[i]:
			j = lps[j-1]
		if P[i] == P[j]:
			j = j + 1
		lps[i] = j
	return lps

def kmp_lps(T,n,P,m) -> list[int,list[int]]:
	lps 	= lps_table(P,m)
	j 		= 0 # numero de caracteres que da match em determinada parte de T
	matches = list[int]()
	
	for i in range(n):
		while j != 0 and P[j] != T[i]:
			j = lps[j-1]
		if P[j] == T[i]:
			j = j + 1
		if j == m:
			matches.append(i-(m-1))
			j = lps[j-1]
	return matches
