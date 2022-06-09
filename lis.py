			
def max_idxval(V,n):
	max_val = V[0]
	max_index = 0
	for i in range(1,n):
		if V[i] > max_val:
			max_val = V[i]
			max_index = i
	return max_index,max_val

#TOP DOWN	
def lis(T, n,*, data = None):
	data = data if data is not None else T

	LIS = [None]*(n)  #--LIS length
	parent = [None]*(n)


	#=======================Montando Tabela de tamanho da LIS=======================
	for i in range(n):
		parent[i] = i 
		LIS[i] = 1
	# -- Começamos do proximo elemento
	for i in range(1,n):
		for j in range(i):
			if T[i] > T[j] and LIS[i] < (LIS[j] + 1):
				LIS[i] = 1 + LIS[j]
				parent[i] = j
	
	#=======================Reconstruindo LIS a partir da tabela=======================
	current, k = max_idxval(LIS,n)
	R = [None]*k
	while k > 0:
		R[k-1] = data[current]
		k = k - 1
		current = parent[current] # troca de ponteiros
	return R

def test():
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

def __main__():
	test()

if __name__ == '__main__':
	__main__()