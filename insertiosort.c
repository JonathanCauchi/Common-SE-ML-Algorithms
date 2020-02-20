
#include <stdio.h>

int main()
{
int a[] = {2,8,5,3,9,4};
int size_a = sizeof(a)/sizeof(int);
int temp;

for(int i=1; i<(size_a); i++)
{
int j = i;

while(j > 0 && a[j-1] > a[j])
{
temp = a[j-1];
a[j-1] = a[j];
a[j] = temp;
j--;

}

}

for (int z=0; z<size_a; z++)
{
printf("%d",a[z]);
}

}
