#include <stdio.h>

int main()
{
int a,b,c;
printf("Enter values for a, b and c: \n");
scanf("%d%d%d",&a,&b,&c);
if((a>b) && (a>c))
{
	printf("A is the greatest");
}
else if((b>a) && (b>c))
{
	printf("B is the greatest");
}
else if((c>a) && (c>b))
{
	printf("C is the greatest");
}
else if((a==b) && (b==c))
{
	printf("All values are the same. Please retry\n");
}

return 0;
}
