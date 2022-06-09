from collections import defaultdict
from ctypes import Array
from email.policy import default

from numpy import array
from utils.perfomance import measure

# d1 < d2 <...< dm in D[1..m]
# Let F(n) be the minimum numbers of coins that amount to 'n' in value
# F(n) = min(F(n-dj))[∀j = 1,2,...,m] + 1, F(0) = 0;
def coin_change(D:Array[int],n:int):
	F = dict()
	m = len(D)
	F[0] = 0	
	for i in range(1,n+1):
		smallest = 0xFFFFFFFF; j = 1
		while j < m and D[j] <= i:
			smallest = min(F[i-D[j]], smallest)
			j += 1
		F[i] = smallest + 1
	return F[n]

def __main__():
	while True:
		n = int(input("Escolha um numero n:"))
		D = [0,1,5,10,20,50,100]
		testfn = coin_change
		testargs = [D,n]
		measure(testfn,*testargs,repeat=1)
		print(f"{testfn(*testargs)=}")
		
if __name__ == '__main__':
	__main__()

