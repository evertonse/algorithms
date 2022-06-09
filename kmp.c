#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

void lps_table(char P[], int m,int lps[]);
void kmp_lps(char T[],int n,char P[],int m);
void printarray(int* arr, int len);
static char *randstr(char *str, int size);

#define new(size,type) (type*)malloc(sizeof(type) * (size))

int main()
{
	int n=1000, m=5;

	char* T = new(n+1,char);
	char* P = new(m+1,char);

	
	randstr(T,n); randstr(P,m);
	
	printf("T = %s\n", T);
	printf("P = %s\n", P);

	kmp_lps(T,n,P,m);
	
	getchar();
}

void printarray(int* arr, int len)
{
	printf("[%d,",arr[0]);
	for (int i = 1; i < len-1; i++)
	{
		printf(" %d,",arr[i]);
	}
	printf(" %d]\n",arr[len-1]);
}

void kmp_lps(char T[],int n,char P[],int m)
{
	printf("inside KMP\n");
	int* lps = (int*) malloc(sizeof(int) * (m)); 
	lps_table(P,m,lps);
	printarray(lps,m);

	for (int i=0, j=0; i<n; i++)
	{
		while(j != 0 && P[j] != T[i])
			j = lps[j-1];
		
		if (P[j] == T[i])
			j++;
		if (j == m-1)
		{
			printf("index: %d found\n",i-m);
			j = lps[j-1];
		}
	}
}

void lps_table(char P[], int m,int* lps)
{
	printf("inside LPS table\n");
	int i, j = 0;
	lps[0] = 0;
	for (i = 1; i < m ; i++)
	{
		while(j != 0 && P[j] != P[i])
			j = lps[j-1];

		if (P[j] == P[i])
			j++;
		printf("lps[%d] = %d\n",i,j);
		lps[i] = j;
	}
	printf("Out LPS table\n");
	printarray(lps,m);
}

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