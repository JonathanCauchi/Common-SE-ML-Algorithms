#include <stdio.h>
#include <math.h>
#include <stdbool.h>
#include <string.h>
//we didnt use any of the fancier function to do this, mostly pure logic, maybe we shouldnt have used strlen tho

int main()
{
int i,j;
char string[20];
printf("Enter string:\n");
scanf("%s",string);
int size = strlen(string);
int count = 0;

for(i=0; i<(round(size/2)-1); i++)
{
if(string[i] == string[(size-1)-i])
{
	count++;
}
}



if(count==(round(size/2))-1)
{
	printf("String is palindrome");
}
else
{
	printf("String is not palindrome");
}

return 0;
}
