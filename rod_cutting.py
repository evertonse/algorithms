#-- n = length of the rod
#-- P = [p0, p1, ..., pn], pi is the price for rod with lengh i
#-- rod(i) = max total sale price of the best cutting of rod of length i
"""
max := P[n]
for i to n :
	r := rod(i) 
	if r + P[n-i] > max:
	max := r + P[n-i] 
"""
def rod_cutting(n, P):
	r = [None]*(n+1)
	r[0] = 0
	r[1] = P[0]
	for i in range(n):
		r[i] = max(r[i-1]) 
		if r + P[n-i-1] > q:
			q = r + P[n-i] 
	return max


def __main__():
	P = [1,5	,8, 9,10, 17,17 ,20,24,30] 
	n = len(P)
	print(rod(n, P))

if __name__ == '__main__':
	__main__()