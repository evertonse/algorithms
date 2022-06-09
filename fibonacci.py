from utils.perfomance import measure


def fib(n:int,*,F=dict()):
	for i in range(n+1):
		if i <= 1:F[i] = i
		else: F[i] = F[i-1] +F[i-2]
	return F[n]

def __main__():
	while True:
		n = int(input("Escolha um numero n:"))
		measure(fib,n,repeat=1)
		print(f"fib({n}) = {fib(n)}")
		
if __name__ == '__main__':
	__main__()

