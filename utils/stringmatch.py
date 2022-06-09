from random import randint
from kmp import kmp_lps,lps_table
from utils.perfomance import measure

randstr = lambda length,ascii=(97,122): ''.join(chr(randint(ascii[0],ascii[1])) for e in range(length))
findall = lambda T,P,overlap=True : _findall_overlapping(T,P) if overlap else _findall(T,P)


def prefix_table (P):
	m = len(P)
	j = 0
	i = 1
	prefix = [0]
	while len(prefix) < m:
		if P[j] == P[i]:
			prefix.append(j+1)
			i += 1
			j += 1
		else:
			if j == 0:
				prefix.append(0)
				i += 1
			if j != 0:
				j = prefix[j-1]
	return prefix

def occurrences(string, sub):
	count = start = 0
	while True:
		start = string.find(sub, start) + 1
		if start > 0:
			count+=1
		else:
			return count

def _findall(T, P):
	def generator():
		start = 0
		while True:
			start = T.find(P, start)
			if start == -1: return
			yield start
			start += len(P) # use start += 1 to find overlapping matches
	return list(generator())

def _findall_overlapping(T:str, P:str) -> list:
	idxs = list()
	start = 0
	while True:
		start = T.find(P, start)
		if start == -1: return idxs
		idxs.append(start)
		start += 1 # use start += 1 to find overlapping matches
	
def naive_match(T,n,P,m):
	matches:list[int] = []
	# shift 0 <= s <= n-m
	for s in range(n-m+1):
		char_match = True
		# test all P[j] == T[s+j]
		for j in range(m):
			if not P[j] == T[s+j]: char_match = False
		
		if char_match:
			matches.append(s)
	return matches

def hash_match(T,n,P,m) -> int or None:
	p_hash = hash(P)
	matches:list[int] = []
	# shift 0 <= s <= n-m
	for s in range(n-m):
		if hash(T[s:s+m]) == p_hash:
			matches.append(s)
	return matches


# Get the next[j]  for a P[0..m]
def next_table(P,m) -> list[int]:
	next = [None]*m
	next[0] = 0
	j = 0; i = 1
	while i < m:
		if P[i] == P[j]:
			next[i] = j + 1
			j = j + 1
			i = i + 1
		else:
			if j == 0:
				next[i] = 0
				i = i + 1
			else:
				j = next[j-1]
	return next

# Get the next[j]  for a P[0..m-1]
def naive_next_table(P,m) -> list[int]:
	next = [None]*m
	next[0] = 0
	for j in range(m):
		for i in range(j-1,-1):
			if P[i] == P[j]:
				i += 1
				j += 1
	return next



def assert_match(fn,T,P):
	n = len(T)
	m = len(P)

	matches = fn(T,n,P,m)

	assert(prefix_table(P) == lps_table(P,m))
	assert(all([T[i:i+m] == P for i in matches]))
	assert(len(matches) == occurrences(T,P))
	assert(len(matches) >= T.count(P))
	assert(len(matches) == len(findall(T,P)))
	assert(matches == findall(T,P,overlap=True))

def __main__():
	n, m = 100000,5
	T = randstr(n,ascii=(97,98))
	P = randstr(m,ascii=(97,98))
	times = 2	


	for fn in [naive_match,kmp_lps,hash_match]:
		fn.out = list()
		measure(fn,T,n,P,m, repeat=times, out=fn.out)
		#assert_match(fn=fn, T=T, P=P,count_idxs=fn.count_idxs)
		
if __name__ == '__main__':
	__main__()

