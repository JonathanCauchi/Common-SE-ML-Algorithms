#include <stdio.h>
#include <stdlib.h> 

struct node
{
	int data;
	struct node* left;
	struct node* right;
};

struct node* newnode(int data)
{
	struct node* node = (struct node*) malloc(sizeof(struct node));
	node->data = data;
	node->right = NULL;
	node->left = NULL;
	return node;
}
void printpreorder(struct node* node)
{
	if(node == NULL)
	{return;}

	printf("%d", node->data);
	printpreorder(node->left);
	printpreorder(node->right);
}

void printpostorder(struct node* node)
{
	if(node == NULL)
	{return;}

	printpostorder(node->left);
	printpostorder(node->right);
	printf("%d", node->data);

}

void printinorder(struct node* node)
{
	if(node==NULL)
	{return;}

	printinorder(node->left);
	printf("%d", node->data);
	printinorder(node->right);
}

int main()
{
	struct node *root = newnode(1);
	root->left = newnode(2);
	root->right = newnode(3);
	root->left->left = newnode(4);
	root->left->right = newnode(5);
	printf("INORDER TRAVERSAL:\n");
	printinorder(root);
	printf("\nPOSTORDER TRAVERSAL:\n");
	printpostorder(root);
	printf("\nPREORDER TRAVERSAL:\n");
	printpreorder(root);
	return 0;
}
