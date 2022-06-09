#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#define new(size,type) (type*)calloc(size, sizeof(type))
#define and &&
#define not !

typedef struct _node
{
	int chr, freq;
	struct _node* left;
	struct _node* right;
} node;


// # For max heap se retornar
// #  0:  a == b
// #  1:  a > b
// # -1:  a < b
// # if you want a min heap, invert the values
int cmp(node a, node b);
void swap(node* a,node* b);


int cmp(node a, node b)
{
	if (a.freq > b.freq)
		return -1;
	if (a.freq == b.freq)
		return 0;
	return 1;
}


//# definning min-heap
int 
isheap(node H[], int n)
{ //# H = array, i = index of root, n = length of array
	int r,l,largest, result = 1;
	for (int i = (int)n/2; i >= 0; i--)
	{
		l = left(i);
		r = right(i);
		largest = i;
		if (l < len(H) and cmp(H[l], H[i]) > 0)
			largest = l;
		if (r < len(H) and cmp(H[r], H[largest]) > 0)
			largest = r;	
		if (largest != i)
			return 0;
	}
	return result;
}
	
int isheap_naive(node H[],int n)
{
	int r,l,largest;
	for (int i = 0; i < n; i++)
	{
		l = left(i);
		r = right(i);
		if (l < n and not cmp(H[i], H[l]) > -1)
			return 0;
		if (r < n and not cmp(H[i], H[r]) > -1)
			return 0;
	}
	return 1;
	
}

	
#/*==================================HEAP START====================================*/

void 
swap(node* a,node* b)
{
	node temp = *a;
	*a = *b;
	*b = temp;
}
  

//#H = heap,i=index
int left(int i){return 2*i+1;}
int right(int i){return 2*i+2;}
int parent(int i){return (i-1)/2;}
	

void 
heapify(node H[], int n, int i)
{
	int r,l,largest;
	l = left(i);
	r = right(i);
	largest = i;
	if (l < n and cmp(H[l], H[i]) > 0)
		largest = l;
	if (r < n and cmp(H[r], H[largest]) > 0)
		largest = r;	
	if (largest != i)
		swap(&H[i],&H[largest]);
		heapify(H,n,largest);
}

void 
buildheap(H,n)
{
	for (int i = n/2; i >= 0; i--)
	{
		heapify(H,n,i);
	}
}

node 
popheap(node H[],int n)
{
	node z = H[0];
	swap(&H[0],&H[n-1]);
	heapify(H,n-1,0);
	return z;
}

void 
bubbleup(node H[],int n, int i)
{
	int p = parent(i);
	if (i < 1)
		return;
	if (cmp(H[i], H[p]) > 0)
	{
		swap(&H[i],&H[p]);
		bubbleup(H,n,p);
	}
}

void //-- H=maxheap; n= heapsize; a=element do insert
insertheap(node H[],int n,node a)
{
	//-- supoe-se ter espaço
	//-- n := n+1
	n = n+1;
	H[n-1] = a;
	bubbleup(H,n,n-1);
}
//*==================================HEAP END====================================*/

	
void printnode(node v)
{
	printf("node->(%d, %c)}",v.freq,v.chr);	
}	


void freq_count(char T[],int n)
{
	//ascii amout of chars
	int i, alph_length = 255;
	int freq_table[] = new(alph_length ,int);

	for (i = 0; i < n; i++)
	{
		freq_table[T[i]] = freq_table[T[i]] + 1;
	}
	return table;
}


void build_trie(int table)
{
	//ascii amout of chars
	int i, alph_length = 255;
	node* H = new(alphabet_size,node);
	n = 0
	for char,freq in table.items()
	{
		node* 
		H.append( node((freq,char)) )
		n += 1
		buildheap(H,len(H))
	}

	for i in range(n-1):
		x = popheap(H,n); n -=1
		y = popheap(H,n); n -=1

		z = node((x.value[0]+ y.value[0], "*"))
		z.left 	= x
		z.right 	= y
		insertheap(H,n,z); n += 1

	return popheap(H,n)
}


void build_encoding_table(root:node,code:list,table:dict):
	if root.value[1] != "*":
		table[root.value[1]] = ''.join(code)
		return
	code.append('0')
	build_encoding_table(root.left, code, table)
	code.pop()
	code.append('1')
	build_encoding_table(root.right, code, table)
	code.pop()

void encode(T,n, root):
	
	map = dict()
	build_encoding_table(root,[],map)

	binary_text = [None]*n*8
	for i in range(n):
		binary_text[i] = map[T[i]]

	assert(len(binary_text) == len(T))
	return "".join(binary_text)

void decode(bits,n, root):
	#--vertice v, ficamos trocando pela esquerda ou direita
	v = root 
	decoded_text = [None]*n; 
	i = 0;j = 0
	while i < len(bits):
		if bits[i] == '0':
			v = v.left
		else:
			v = v.right
		
		char = v.value[1]
		if char != "*":
			decoded_text[j] = char
			j = j + 1
			v = root
		i = i + 1
	return "".join(decoded_text)

void programa(T,n):
	table = freq_count(T,n)
	root = build_trie(table)
	
	binary_text = encode(T,n , root)
	print(binary_text)
	
	decoded_text = decode(binary_text,n, root)
	print(decoded_text)
	
static char *randstr(char *str, int size)
{
   //const char charset[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJK...";
	const char charset[] = "xy";
	if (size) {
		--size;
		for (int n = 0; n < size; n++) {
				int key = rand() % (int) (sizeof charset - 1);
				str[n] = charset[key];
		}
		str[size] = '\0';
	}
    return str;
}
void main()
{
	int n = 100
	T = randstr(n,ascii=(97,98))
	T = "Random thing I'm random"; n = len(T)
	programa(T,n)

}

if __name__ == '__main__':
	__main__()