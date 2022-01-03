#include "fibonacci.h"

unsigned long int fib(int n) {
	int i;
	unsigned long int a, b, tmp;
	a = 0; b = 1;
	for (i=0; i<n; i++) {
		tmp = a; 
		a = b; 
		b = tmp + b;
	}
	return a;
}

