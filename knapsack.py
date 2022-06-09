"""
	Items[1..n]      = (item_1, item_2, ... , item_n )
	Value[1..n]       = (v_1,v_2,...,v_n )
	Weight[1...n] =(w_1,w_2,...,w_n )
	W  = Maximum Capacity
"""
#UKP (Unbouded Knapsack Problem)
from collections import defaultdict
from random import randint
from sqlalchemy import true


def Uknapsack(
	n: int,
	W:	int,
	w: list[int],
	v: list[int]):
	m = dict()
	m[0] = 0
	pass
		 
def binary_knapsack(
		n: int, 	W:	int,
		w: list[int], v: list[int]
	) -> int:

	m = dict()
	for i in range(n+1):
		m[i,0] = 0
	for j in range(W+1):
		m[0,j] = 0
	
	for i in range(1, n+1):
		for j in range(W+1):
			# Nesse caso eu não posso adicionar o atual porque 
			# No caso binário, se o item de peso w[i] não pode ser adicionado 
			# (porque é maior que o peso j permitido para essa iteração)
			# Então m[i,j] deve ser o mesmo que desconsiderando o item atual
			maxvalue_do_item_anterior_mesmo_peso = m[i-1,j]
			if w[i-1] > j:
				m[i,j] = maxvalue_do_item_anterior_mesmo_peso
			else:
				# incluindo o item atual, decidimos qual o maior
				# repare que se incluimos esse item, temos um incremento de v[i] no valor total dessa iteração
				# e ainda, devemos somar com o maior valor possivel de j-w[i], que seria o maior permitido
				m[i,j] = max(v[i-1]+m[i-1, j-w[i-1]] ,maxvalue_do_item_anterior_mesmo_peso)
	

	return m[n,W],find_iterative(n,W,w,m)

# retorna o conjunto de indices que estão incluidos no problema
def find_recursive(i,j,w, m):
	if i == 0:
		return {}
	if m[i, j] > m[i-1, j]:
		return {i-1,*find_recursive(i-1, j-w[i-1] ,w,m)}
	else:
		return find_recursive(i-1, j, w,m)
	
def find_iterative(n,W, w,m):
	S = set()
	#i = n
	j = W
	for i in range(n,0,-1):
		if m[i, j] > m[i-1, j]:
			S.add(i-1)
			j = j - w[i-1]
	return S
	
def exact_knapsack(S,n, K):
	P = dict() ; included = defaultdict(lambda x:False)
	P[0,0] = True
	for k in range(1, K+1): 
		P[0, k] = False
	# Opcional , vai ser computado no loop abaixo através d P[0, 0]
	for i in range(n): 
		P[i, 0] = True

	for i in range(1,n): 
		for k in range(K+1): 
			if P[i-1,k] == True:
				P[i,k] = True

			elif S[i-1] <= k and P[i-1, k-S[i-1]]:
				P[i,k] = True
				included[i,k] = True
			else:
				P[i,k] = False
	return P[i,k], included

def test1():
	n = 18
	A = [randint(0,100) for i in range(n)]
	W = sum(A)//2
	
	total,partition = binary_knapsack(n,W,A,A)
	
			
	print(f'total = {total}')
	print(f'A = {A} sum = {sum(A)}')
	
	print(f'W = sum/2 = {W}')
	
	print(f'{partition=}')
	bro = [A[i] for i in range(n) if i not in partition]
	meu = [A[i] for i in range(n) if i in partition]
	
	print(f'bro = {bro} sum = {sum(bro)}')
	print(f'meu = {meu} sum = {sum(meu)}')

def test2():
	n = 10
	w = [0]*(n+1)
	v = [0]*(n+1)
	w[1]=23;	w[2]=26;	w[3]=20;	w[4]=18;	w[5]=32;	w[6]=27;	w[7]=29;	w[8]=26;	w[9]=30;	w[10]=27
	v[1]=505;v[2]=352;v[3]=458;v[4]=220;v[5]=354;v[6]=414;v[7]=498;v[8]=545;v[9]=473;v[10]=543
	W = 67
	max_value =	binary_knapsack(n,W, w, v)
	print(max_value)

	print(exact_knapsack(w,n+1,W))

def __main__():
	test1()

if __name__ == '__main__':
	__main__()