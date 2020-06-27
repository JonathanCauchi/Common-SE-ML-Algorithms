
#include <stdio.h>
#include <stdlib.h>

struct node
{
	int value;
	struct node *next;
};

void printlist(struct node *p)
{
while(p != NULL)
{
	printf("%d\n",p->value);
	p = p->next;
}
}

void reverselist(struct node *p)
{
int prev = NULL


}


int main()
{
struct node *head;
struct node *first = NULL;
struct node *second = NULL;
struct node *third = NULL;

first = malloc(sizeof(struct node));
second = malloc(sizeof(struct node));
third = malloc(sizeof(struct node));

first->value = 1;
second->value = 2;
third->value = 3;

first->next = second;
second->next = third;
third->next = NULL;

head = first;
printlist(head);
print("---------------")
reverselist(head);
printlist(head);
return 0;
}
