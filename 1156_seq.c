#include <stdio.h>

int main() {
	int i, d;
	float s;

	d = 1;
	s = 0.0;
	for (i = 1; i < 40; i = i+2) {
		/* printf("%d / %d\n", i, d); */
		s = s + (float)i / d;
		d = d * 2;
	}

	printf("%.2f", s);

	return 0;
}