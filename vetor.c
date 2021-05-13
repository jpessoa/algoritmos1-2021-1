#include <stdio.h>
#include <stdlib.h>

#define MAX 100

int main() {
	int n;
	int vet[MAX];
	int i;
	int *x;

	printf("Tamanho do vetor? ");
	scanf("%d", &n);

    x = malloc(n * sizeof(int));
    if (x == NULL) {
    	printf("Não tem memória!!");
    	exit(EXIT_FAILURE);
    }

    /*

    for (i = 0; i < n; i++) {
		x[i] = 7;
	}


	for (i = 0; i < n; i++) {
		printf("%d\n", x[i]);
	}
	*/

	free(x);
	
	return 0;
}