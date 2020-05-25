#include<stdio.h>

void main()
{
int x,y;
int i,j;
printf("Enter size of coordinates X & Y matrix:\n");
scanf("%d%d",&x,&y);
int array1[x][y], array2[x][y], sarray[x][y];
printf("Enter values of matrix 1:\n");
for(i=0; i < x; i++)
{
	for(j=0; j<y; j++)
	{
		scanf("%d",&array1[i][j]);
	}
}
printf("Enter values for matrix 2:\n");
for(i=0; i<x; i++)
{
	for(j=0; j<y; j++)
	{
		scanf("%d",&array2[i][j]);
	}
}
for(i = 0;i<x; i++)
{
	for(j=0;j<y;j++)
	{
		sarray[i][j] = array1[i][j] + array2[i][j];
	}
}
printf("Sum of matrices is equal to:\n");
for(i = 0; i<x; i++)
{
	for(j=0; j<y;j++)
	{
		printf("%d",sarray[i][j]);
	}
printf("\n");
}


}

