#include <stdio.h>

int main()
{
int num, limit;
printf("Enter number to generate table:\n");
scanf("%d",&num);
printf("Enter multiplication limit: \n");
scanf("%d",&limit);
for(int i = 1; i <= limit; i++ )
{
	printf("%d * %d = %d\n",num,i,(num*i));

}

return 0;
}
