from collections import defaultdict
from kmp import kmp_lps
from utils.stringmatch import hash_match, naive_match, randstr,findall,assert_match
from utils.perfomance import measure

def shift_table(P:str, m:int) -> defaultdict:
	table = defaultdict[str,int](lambda:m)
	for j in range(m-1):
		table[P[j]] = m -1 -j
	return table

def hoorspool(T,n, P,m):
	matches = list[int]()
	table = shift_table(P,m)
	i = 0
	while i < n-m+1:
		k = m - 1 
		while k >= 0 and P[k] == T[i+k]:
			k = k - 1 
		if k < 0:
			matches.append(i)
		i = i + table[T[i+m-1]]
	return matches


def __main__():
	n, m = 1000,4
	T = randstr(n,ascii=(97,98))
	P = randstr(m,ascii=(97,98))
	assert_match(hoorspool,T,P),
	
	times = 100
	for fn in [hoorspool,naive_match,hash_match,kmp_lps]:
		fn.out = list()
		measure(fn,T,n,P,m, repeat=times, out=fn.out)
		assert_match(fn,T,P),
		#assert_match(fn=fn, T=T, P=P,count_idxs=fn.count_idxs)
		
if __name__ == '__main__':
	__main__()

