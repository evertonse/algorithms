from random import randint

def coin_collect(board,n,m):
	
	DP = dict()
	DP[0,0] = board[0][0]
	for i in range(1,n):
		DP[i,0] = DP[i-1,0] + board[i][0]
	for j in range(1,n):
		DP[0,j] = DP[0,j-1] + board[0][j]

	for i in range(1,n):
		for j in range(1,m):
			DP[i,j] = max(DP[i-1,j], DP[i,j-1])+board[i][j]
			
	return DP[n-1,m-1] 
def __main__():
	n = 10
	m = 10
	board = [[randint(0,1) for i in range(m)] for i in range(n)]
	max_coins = coin_collect(board, n , m)
	print(
		board,
		f"\nmaximo de coins nesse board: {max_coins}"
	)

if __name__ == '__main__':
	__main__()