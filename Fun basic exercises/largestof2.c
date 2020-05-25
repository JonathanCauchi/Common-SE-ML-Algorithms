#include <stdio.h>
#include <stdlib.h>
int largest(int n, int m)
{
	if(n>m)
	return n;
	else if(m > n)
	return m;
	else
	printf("Same values, try again");
	exit(0);
}

int main()
{
int num1,num2;
printf("Enter 2 numbers:\n");
scanf("%d%d",&num1,&num2);
int result = largest(num1,num2);
printf("Largest number is: %d",result);
return 0;

}
