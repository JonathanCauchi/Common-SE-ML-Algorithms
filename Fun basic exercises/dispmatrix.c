#include <stdio.h>

void main()
{
int X,Y;
printf("Enter size of X coordinate:\n");
scanf("%d",&X);
printf("Enter size of Y coordinate:\n");
scanf("%d",&Y);
int array[X][Y];
printf("Enter values of matrix (1st row, then 2nd...)\n");
for(int i=0; i<X;i++)
{
	for(int j=0; j<Y; j++)
	{
		scanf("%d",&array[i][j]);
	}
}
for(int k=0; k<X; k++)
{
	for(int l=0; l<Y; l++)
	{
		printf("%d",array[k][l]);
	}
printf("\n");
}
	
//TO DO TRANSPOSE JUST SHIFT LOOPS

}
