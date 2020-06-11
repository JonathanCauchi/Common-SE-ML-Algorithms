#include <stdio.h>

void inputarray(int *arr, int size);
int searcharray(int *arr, int size, int search);
int main()
{
int array_size;
int array[array_size];
int search;
printf("Enter size of array:\n");
scanf("%d",&array_size);
printf("Enter numerical elements:\n");
inputarray(array, array_size);

printf("Enter element to search:\n");
scanf("%d",&search);
int index = searcharray(array, array_size, search);

if(index == -1)
{
	printf("INexistent element");
}else{
	printf("%d is the index:",index);
}
return 0;
}

void inputarray(int *arr,int size)
{
	int *arrayend = arr + size - 1;
	while( arr <= arrayend)
	{
		scanf("%d",arr++);
	}
}

int searcharray(int *arr, int size, int search)
{
	int index = 0;
	int * arrayend = arr + size - 1;	
	
	while(arr <= arrayend && *arr!=search)
	{
		arr++;
		index++;
	}

	if(*arr = search)
		return index;

	return -1;
}
