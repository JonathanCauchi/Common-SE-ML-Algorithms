#include <stdio.h>
int fibonacci(int n);

int main()
{
int num = 20;
int fib = 0;
for(int i=0; i<20; i++)
{
printf("%d\n",fibonacci(fib));
fib++;
}
}

int fibonacci(int n)
{
if(n==0)
{
return 0;
}
else if(n == 1)
{
return 1;
}
else if(n==2)
{
return 1;
}
else
{
return (fibonacci(n-1)+fibonacci(n-2));
}

}
