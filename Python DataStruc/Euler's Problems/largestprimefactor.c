

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int isprime(long int num);

int isprime(long int num)
{
int i;
for(i=2; i<=num; i++)
{
	if(num%i==0)
	{
		return 1;
	}
}

return 0;
}



int main()
{
long int num = 600851475143;
long int i;
int array[10000];

for(i=2; i<=num; i++)
{
	if(isprime(i)==0)
	{
		if(num%i==0)
		{
			printf("%ld",i);
		}	
	}
}


return 0;
}
