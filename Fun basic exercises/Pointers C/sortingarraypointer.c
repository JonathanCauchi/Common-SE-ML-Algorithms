#include <stdio.h>
#include <stdlib.h>
#define MAX 100

void inputarray(int *arr, int size);
void printarray(int *arr, int size);
void sortascending(int *arr, int size);

int main()
{
int array_size, array[MAX],choice;
printf("Enter size of array:\n");
scanf("%d",&array_size);
//array_size -= 1;
printf("Enter elements:\n");
inputarray(array, array_size);
printf("Sorting scending:\n");
sortascending(array, array_size);

printarray(array, array_size);

return 0;
}


void inputarray(int *arr, int size)
{
	int *arrayend = arr + size - 1;
	while(arr <= arrayend)
	{
		scanf("%d\n",arr++);
	}

}

void printarray(int *arr, int size)
{
	int *arrayend = arr + size-1;
	while(arr <= arrayend)
	{		
		printf("%d", *(arr));
		arr++;
	}
}


void sortascending(int *arr, int size)
{
	int *arrayend = arr + size - 1;	
	int i,j,t;
	for(i=0; i< size; i++)
	{
		for(j=i+1; j< size; j++)
		{
			if(*(arr+j)<*(arr+i))
			{
				t = *(arr+i);
				*(arr+i) = *(arr+j);
				*(arr+j) = t;
			}
		}
	}		
}



