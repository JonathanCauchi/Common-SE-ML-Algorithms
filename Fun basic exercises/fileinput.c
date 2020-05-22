#include <stdio.h>
#include <stdlib.h>

int main() {
 
char c[100];
FILE *fptr;

if((fptr = fopen("read.txt","r")) == NULL)
{
	printf("Error reading file");
	exit(1);
}
else
{
	fscanf(fptr, "%s",c);
	printf("%s", c);
}
return 0;
}
