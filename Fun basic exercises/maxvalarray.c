#include <stdio.h>

int main()
{
int array[100];
int num;
printf("Enter array size (not more than 100): \n");
scanf("%d",&num);
printf("Enter individual elements:\n");
for(int i=1 ; i<=num; i++)
{
    scanf("%d",&array[i]);

}
int max = array[0];
for(int j=1; j <= num; j++)
{
   if(array[j]>max)
	max = array[j];	
}

printf("Largest value in array is: %d",max);

return 0;
}
