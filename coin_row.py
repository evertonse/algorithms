"""EXAMPLE 1 Coin-row problem There is a row of n coins whose values are some
positive integers c1, c2, . . . , cn, not necessarily distinct. The goal is to pick up the
maximum amount of money subject to the constraint that no two coins adjacent
in the initial row can be picked up"""
def coin_row(C, n,*, memo = dict()):
	memo[0] = 0
	memo[1] = C[0]
	
	if n in memo:
		return memo[n]
	
	include 		= C[n-1]  + coin_row(C, n-2)
	not_include = coin_row(C, n-1)

	result = max( include, not_include )
	memo[n] = result
	
	return result

def coin(C,n):
	if n == 0:
		return 0
	if n == 1:
		return C[0]
	return max(coin(C, n-1) , C[n-1]+ coin(C, n-2))

def __main__():
	C = [5,1,2,10,6,2]
	n = len(C)
	print(
		coin_row(C,n)
	)
	print(
		coin(C,n)
	)
if __name__ == '__main__':
	__main__()