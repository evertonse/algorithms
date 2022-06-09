#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int max(int a, int b);
int lcs(char T[], int n, char P[], int m);

typedef char* str;
typedef int32_t;

int lcs(
	str T, int n,
	str P, int m) 
{
	int LCS[n+1][m+1];

	for (size_t i=0; i < n+1; i++) 
		LCS[i][0] = 0; 
	for (size_t j=0; j < m+1; j++)
		LCS[0][j] = 0;
	
	for (int i = 1; i < n+1; i++)
		for (int j = 1; i < m+1; i++) {
			if (T[i] == P[j])
				LCS[i][j] = 1 + LCS[i-1][j-1];
			else {
				LCS[i][j] = max(LCS[i][j-1],LCS[i-1][j]) ;
			}
		}
	return LCS[n][m];
}

int max(int a, int b) {
	return a > b ? a : b;
}

int main() {
	char T[] = "AGGTAB";
	int n = strlen(T);
	
	char P[] = "GXTXAYB";
	int m = strlen(P);
	
	int a = lcs(T,n, P,m);

	printf("%i",a);
}