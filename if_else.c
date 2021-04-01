#include <stdio.h>

int main() {
	int x;

	scanf("%d", &x);

    if (x > 0) {
    	printf("%d é positivo.", x);
	} else {
		printf("%d é negativo.", x);
	}

	return 0;
}