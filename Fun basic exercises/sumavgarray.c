#include <stdio.h>

void main()
{
float array[10],sum, avg;
sum = 0; 
printf("Enter 10 numbers to be inserted in array:\n");
for(int i=0 ; i<10; i++)
{
	scanf("%f",&array[i]);
	sum += array[i];
}

printf("Sum is equal to: %f\n",sum);
size_t size = sizeof(array)/sizeof(array[0]);
avg = sum/size;
printf("Average is equal to: %f",avg);
}
