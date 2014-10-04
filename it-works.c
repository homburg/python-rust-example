#include <stdio.h>

extern void it_works(const char *input, int j)
{
	printf("Hello, C! say: %s (%d)\n", input, j);
}
