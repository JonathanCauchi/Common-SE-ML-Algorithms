#include <stdio.h>
#include <stdlib.h>

int main()
{
float num1, num2;
float *pt1, *pt2;
pt1 = &num1;
pt2 = &num2;
printf("Enter 2 numbers to add:\n");
scanf("%f%f",&num1,&num2);
float result = *pt1 + *pt2;
printf("Sum is: %f",result);
return 0;

}
