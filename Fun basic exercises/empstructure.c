#include<stdio.h>

struct employee
{
	char id[20];
	char name[50];
	char position[30];
	float salary;
};

int main()
{

struct employee employee;
printf("Enter name:\n");
scanf("%s",employee.name);
printf("Enter ID:\n");
scanf("%s",employee.id);
printf("Enter position:\n");
scanf("%s",employee.position);
printf("Enter salary:\n");
scanf("%f",&employee.salary);

printf("Name: %s\n",employee.name);
printf("ID: %s\n",employee.id);
printf("Positon: %s\n",employee.position);
printf("Salary: %f\n",employee.salary);

return 0;
}
