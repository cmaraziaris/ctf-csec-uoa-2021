
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "base64.h"


#define SIZE 100

char user_input[] = "FwwXDBcMEyMw==";


int main(int argc, char const *argv[])
{
	unsigned char *buf = malloc(SIZE * sizeof(unsigned char));


	char *input = strdup(user_input);
	size_t size = strlen(input);


	fprintf(stderr, "Input is: %s\n", input);
	Base64Decode(input, &buf, &size);
	fprintf(stderr, "Output is: %s\n", buf);


	return 0;
}