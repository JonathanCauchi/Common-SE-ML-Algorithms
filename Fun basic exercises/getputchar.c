
#include <stdio.h>
#include <stdlib.h>

int main()
{
int  c;
printf("ENTER STRING");
while((c = getchar()) != EOF)
{
	putchar(c);
}
return 0;
}

/////////////////////////////////

#include <stdio.h>
#include <stdlib.h>

int main()
{
int  c;
printf("ENTER STRING");
while(1)
{
	c = getchar();
	if(c == EOF){break;}	
        putchar(c);
}
return 0;
}




