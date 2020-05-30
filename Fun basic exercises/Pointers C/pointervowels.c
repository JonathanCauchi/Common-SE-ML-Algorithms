#include <stdio.h>
#include <string.h>
int main()
{
int i;
int count = 0;
char str[50];
char *ptr;
ptr = str;
printf("Enter sentence:\n");
scanf("%s",str);
int size = strlen(str);
for(i=0;i<size;i++)
{
	if(ptr[i]=='a'||ptr[i]=='e'||ptr[i]=='i'||ptr[i]=='o'||ptr[i]=='u')
	{
		count++;
	}
}
printf("Vowel count: %d",count);
return 0;
}
