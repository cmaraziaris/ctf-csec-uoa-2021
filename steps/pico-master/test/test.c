

#include <stdlib.h>
#include <string.h>

int main(int argc, char const *argv[])
{
	char s1[] = "peaki";
	char s2[] = "pea";


	s1[3] = 0;

	printf("%d\n", strcmp(s1, s2));

	return 0;
}