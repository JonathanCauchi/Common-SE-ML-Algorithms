
#include <stdio.h>
#include <stdlib.h>

enum state
{
idle = 0,
waiting = 1,
being_served = 2,
exiting = 3
};

int main()
{
int state = idle;
int flag = 0;
while(flag == 0)
{
int option;
printf("What is your current state?\n");
printf("1-Waiting, 2-Being served, 3-Exiting\n");
scanf("%d",&option);
	
//Ideally, use switch case statements given they're more efficient (better optimization during compiling)
if(option == 1)
{
	state = waiting;
	printf("State is waiting\n");
	printf("%d\n",state);
}
if(option == 2)
{
	state = being_served;
	printf("State is being served\n");
	printf("%d\n",state);
}	
if(option == 3)
{
	state = exiting;
        printf("Exiting\n");
        printf("%d\n",state);
        exit(0);
}
if(option < 1 && option > 3)
{
	printf("Invalid input\n");
}

}




return 0;
}

