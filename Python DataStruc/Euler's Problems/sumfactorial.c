

#include <stdio.h>
#include <stdlib.h>
#include <string.h>


//Data type conversion is more challenging that I thought it would be

int factorial(int num);

int factorial(int num)
{
if(num == 1)
{
	return 1;
}else
{
	return num*factorial(num-1);
}
}

int main()
{
int num;
char str[20];
int i;
printf("Enter number: \n");
scanf("%d",&num);
int fact = num;
int result = factorial(fact);
sprintf(str,"%d",result);
printf("Factorial: %d\n", result);
size_t size = sizeof(str)/sizeof(char);
int total = 0;
for( i = 0; i < size; i++)
{
	printf("%c",str[i]);
	total += ((int)(str[i]));
}
printf("Total of fact digits: %d",total);
return 0;
}
