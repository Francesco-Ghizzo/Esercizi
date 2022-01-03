#include <stdio.h>
#include "fibonacci.h"

#define MAX 50

int main() {
        int i;
	for (i=1; i<MAX+1; i++) {
                printf("%lu, ", fib(i));
        }
}

