#include <stdio.h>

int main() 
{
const b = 7;
int i, j, temp;
int list[b] = {7, 3, 8, 5, 2, 9, 6};


for(j=1; j < b; j++ )
{
  temp = list[j];
  i = j-1;

 while(temp<list[i])
 {
   list[i+1]=list[i];
   i=i-1;
 }
list[i+1]=temp;

}


for ( int c=0; c < b; c++){
  printf("%d",list[c]);
}



}


