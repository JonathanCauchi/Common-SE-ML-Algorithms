#include <stdio.h>
#include <string.h>
int main()
{
char array[100];
printf("Enter number/string (sequence of characters): \n");
scanf("%s",array);
int length = strlen(array);
printf("Reversed sequence is: \n");
for(int i = length; i >= 0; i--)
{
printf("%c",array[i]);
}

return 0;
}
