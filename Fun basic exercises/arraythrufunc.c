#include <stdio.h>

int *getarray()
{
static int array[10];
for(int i=0; i<5; i++)
{
    array[i]=i+1;
}

return array;

}

int main()
{
int *p;
p = getarray();
for(int i=0; i<5; i++)
{
    printf("%d\n",*(p+i));//pointer keeps incrementing to next location in array
}
return 0;
}
