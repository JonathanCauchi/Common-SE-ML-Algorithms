#include <stdio.h>
#include <stdlib.h>
int main()
{
	double A[5] = {
	[0] = 4.5,
	[1] = 56.2,
	[2] = 23.5,
	[3] = 122.1,
	[4] = 23.9,
	};

	for(int i = 0; i < 5; i++)
	{
		printf("Element no %d has a value of %g\n", i, A[i]); 
		//%g takes float
	}

return EXIT_SUCCESS;


}
