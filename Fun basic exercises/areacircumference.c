#include <stdio.h>
#include <math.h> //so to use pow() function
#define PI 3.14159265358979323846

int main()
{
float radius;
printf("Enter radius of circle:\n ");
scanf("%f",&radius);
float result = radius * radius;
float area = PI *  result;
float circumference = 2 * (PI * radius);
printf("Area of circle is equal to: %f\n", area);
printf("Circumference of circle is equal to: %f\n", circumference);


return 0;
}
