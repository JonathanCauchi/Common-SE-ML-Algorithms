#include <stdio.h>

int factorial(int n);

int factorial(int n)
{
	if(n==0 || n==1)
	return 1;
	while(n>1)
	{
		return (n*factorial(n-1));
	}

}


int main()
{
int num;
printf("Enter num: \n");
scanf("%d",&num);
int result = factorial(num);
printf("Factorial of %d is equal to: %d\n",num, result);
return 0;

}
