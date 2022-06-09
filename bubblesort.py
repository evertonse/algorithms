from random import randint


def bubblesort(V:list ,n:int) -> None:
	for i in range(n-1):
		for j in range(n-1):
			if V[j] > V[j + 1] :
				temp = V[j] 
				V[j] =  V[j + 1]
				V[j + 1] = temp

def __main__():
	n = 100
	V1 = [randint(-100, 100) for i in range(n)]
	V2 = V1.copy()
	
	assert(V1 == V2)
	bubblesort(V1,n)
	V2.sort()
	assert(V1 == V2)
	print(f"{V1=}")
	print(f'{V2=}')
if __name__ == '__main__':
	__main__()