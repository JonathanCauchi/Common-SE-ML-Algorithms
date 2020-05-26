#include <stdio.h>

int main()
{
int x,y,i,j;
printf("Enter x & y coordinate sizes:\n");
scanf("%d%d",&x,&y);
printf("MULTIPLICATION TABLE\n");
printf("------------------\n");
for(i=1;i<=x;i++)
{
for(j=1;j<=y;j++)
{
	printf(" %d -",i*j);
	if(j==y)
	printf(" %d",i+j);
}
printf("\n");
}
return 0;
}
