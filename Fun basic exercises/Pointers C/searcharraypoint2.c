#include <stdio.h>
#define MAX 100

void inputarray(int *arr, int size);
int searcharray(int *arr, int size, int value);

int main()
{
int size_array;
int array[MAX];
int value;
printf("Enter size of array:\n");
scanf("%d",&size_array);
printf("Enter elements into array:\n");
inputarray(array, size_array);
printf("Enter element to search and return index:\n");
scanf("%d",&value);
int index = searcharray(array, size_array, value);
if(index == -1)
{
	printf("%d does not exist in list", value);
}else{
	printf("Value found at index: %d",index);
}
return 0;
}

void inputarray(int *arr, int size)
{
	int *arrend = arr+size-1;
	while(arr <= arrend)
	{
		scanf("%d",arr++);
	}
}

int searcharray(int *arr, int size, int value)
{
	int *arrend = arr+size-1;
	
	int index = 0;
	while(arr<=arrend && *arr!=value)
	{
		arr++;
		index++;
	}

	if(*arr = value)
	{
		return index;
	}
	
return -1;

}


