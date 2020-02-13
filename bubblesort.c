#include <stdio.h>

int main()
{

int a[]= {3,2,6,5,7,1};
int a_size = sizeof(a)/sizeof(int);
int i,j,temp;

//int loop = a_size;

for(i=0;i<a_size;i++)
{

  for(j=i+1;j<a_size;j++)
  {

    if(a[i]>a[j])
    {
      temp = a[i];
      a[i] = a[j];
      a[j] = temp;
    }
    else
    {
      continue;
    }

//loop--;
}

}

for(int c=0; c<a_size; c++)
{
  printf("%d",a[c]);
}

}
