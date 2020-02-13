
#include <stdio.h>

int main()
{

int a[] = {3, 2, 6, 4, 9, 7};
int a_size;
int i,j,temp;
//temp = a[0];
a_size = sizeof(a)/sizeof(int);


for(j=0;j<(a_size);j++)
{

int location = a[j];

for(i=j+1;i<(a_size);i++)
{
   if(location < a[i])
   {
      continue;
   }
   else if(location > a[i])
   {
      location = a[i];
   }
  //if swap func exists, call here
  temp = a[j];
  a[j] = location;
  a[i] = temp;
}

  
}

for ( int c=0; c < a_size; c++)
{
  printf("%d",a[c]);
}



}
