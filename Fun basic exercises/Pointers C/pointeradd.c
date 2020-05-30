#include <stdio.h>

void main()
{
int i,j;
int *ptr1, *ptr2;
printf("Enter 2 numbers:\n");
scanf("%d%d",&i,&j);
ptr1 = &i;
ptr2 = &j;
int result =*ptr1+*ptr2;
printf("Total is %d",result);

}
