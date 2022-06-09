"""
T = t1,t2,...,tn

Maior parte dos problemas de duas variaveis precisa de uma matriz e tempo constante de avaliação
ou podentos ter uma quantidade linear de subproblemas e avaliação linear então O(n^2)
lis(i) := i indica T[i:], onde i está incluso

função "se começar em i qual é lis(i)":
	P = vetor[1..n] -- possiveis valores
	para j de i-1 até n:
		P[j] = 0 -- default
		se T[i] < T[j] então: --garantir a subsequencia crescente
			P[j] = lis(j)
	-- assume-se i está incluso
	-- max(Iterable) <- Retornar o maior valor de P
	return lis(i) = 1 +  max(P)

algoritmo LIS(T,n):
	P = vetor[1..n] -- possiveis valores
	para i de 0 até n faça:
		P[i] = lis(i)
	return max(P)

		

"""


from lcs import lcs


infty = 0xFFFFFF




def lis_len_reversed(T, n):
	LIS = [None]*(n+1); LIS[n] = 0
	for i in reversed(range(n+1)):
		P = [0]*(n+1)
		for j in range(i+1,n+1):
			P[j] = 0
			if T[i-1] < T[j-1]:
				P[j] = LIS[j]
		LIS[i] = 1 +  max(*P)
	return max(*LIS)

def lis_copy(T, n):
	LIS = [None]*(n)  #--LIS length
	L = [[]]*(n)		#--LI  sequence
	L[0].append(T[0])
	for i in range(n):
		LIS[i] = 1

	for i in range(1,n):
		for j in range(i):
			if T[i] >= T[j] and LIS[i] < (LIS[j] + 1):
				LIS[i] = 1 +  LIS[j] 
				L[i] = L[j].copy()
		
		L[i].append(T[i])
	
	max_index 	= None
	max_val 		= -1
	for i in range(n):
		if LIS[i] > max_val:
			max_val 	 = LIS[i]
			max_index = i
	
	print(L[max_index], f"of lenth {max_val}")
	assert(len(L[max_index]) == max_val)
	return max(*LIS)

#TOP DOWN	
def lis_table(T, n):
	LIS = [None]*(n)  #--LIS length
	parent = [None]*(n)
	for i in range(n):
		parent[i] =i 
		LIS[i] = 1
	# -- Começamos do proximo elemento
	for i in range(1,n):
		for j in range(i):
			if T[i] > T[j] and LIS[i] < (LIS[j] + 1):
				LIS[i] = 1 + LIS[j]
				parent[i] = j
	
	print(f'{parent=}') 
	return LIS

def lis(T, n,*, data=None):
	data = data if data is not None else T
	LIS = lis_table(T, n)
	i = max_index(LIS, n)
	R = [data[i]]
	# -- Não precisamos olhar para valores depois de i apenas antes, 
	# -- visto que, a tabela sempre for computado em relação a um  j < i <= n
	# -- Então DEVE existir um j tal que LIS[j] = L[i]-1,
	# -- e é garantidtido que T[j] < T[i], portanto podemos 
	# -- concatenar T[i] ao final da maior subsequencia dada por T[:j]
	for j in range(i,-1,-1):
		if LIS[j] == LIS[i]-1:
			i = j 
			R.insert(0,data[j])
	return R
			
def max_index(V,n):
	max_val = V[0]
	max_index = 0
	for i in range(1,n):
		if V[i] > max_val:
			max_val = V[i]
			max_index = i
	return max_index


def test1():
	datas = [
		"01/02/2021",
		"02/02/2021",
		"03/02/2021",
		"04/02/2021",
		"05/02/2021",
		"06/02/2021",
		"07/02/2021",
		"08/02/2021",
		"09/02/2021"]
	
	mortes = [ 800,900,850,955,750,1100,1005,1215,1155]
	
	n = len(mortes)

	print(f"original arr = {mortes} \n lis =",
		lis(mortes,n, data=datas),"\n")

def test2():
	arr = [-1,3,4,5,2,2,2,2]
	n = len(arr)
	print(f"original arr = {arr} \n lis =",
		lis(arr,n),"\n")

	arr = [10,22,9,33,21,50,41,60] ; n = len(arr)
	print(f"original arr = {arr} \n lis =",
		lis(arr,n),"\n")

def __main__():
	tests = [test1,test2]
	for test in tests:
		test()

if __name__ == '__main__':
	__main__()