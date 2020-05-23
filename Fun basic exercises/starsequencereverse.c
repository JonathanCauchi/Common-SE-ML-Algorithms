#include <stdio.h>

int main()
{
int num;
printf("Enter number of layers: \n");
scanf("%d",&num);
for(int i = 1; i <= num; i++)
{
	for(int j = num; j>=i ; j--)
	{
	printf(" ");
	}
	for(int k=1; k<=i; k++)
	{
	printf("*");
	}	
	printf("\n");
}
return 0;
}
