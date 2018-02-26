#include <stdio.h>
#include <stdlib.h>

typedef struct number{
	int a;
	struct number *left;
	struct number *right;
} node;
typedef node* NODE;

NODE insert(int x, NODE tree);

void preorder(NODE tree);
void inorder(NODE tree);
void postorder(NODE tree);

int main()
{
	FILE *f;
	int num[30]; // array for reading file
	int i;

	NODE tree;

	// creat root
	tree = (node *)malloc(sizeof(node));
	tree->a = 0;
	tree->left = NULL;
	tree->right = NULL;


	f = fopen("tree_traversal.txt","r");
	if(f == NULL){
		printf("file open error!\n");
		exit(0);
	}

	// create tree
	for(i=0; i<8; i++)
	{
		fscanf(f1, "%d", &num[i]);
		tree = insert(num[i], tree);
	}

	printf("tree_traversal.txt : \n\n");

	printf("preorder : \t");
	preorder(tree->right);

	printf("\n\ninorder : \t");
	inorder(tree->right);

	printf("\n\npostorder : \t");
	postorder(tree->right);

	printf("\n\n");
	fclose(f);
}


NODE insert(int x, NODE tree)
{

	NODE temp = tree;
	NODE cur;

	cur = (node *)malloc(sizeof(node));

	cur->a = x;
	cur->left = NULL;
	cur->right = NULL;

	while(1){

		if(x < temp->a){
			if(temp->left == NULL) break;
			temp = temp->left;			
		}else{
			if(temp->right == NULL) break;
			temp = temp->right;			
		}
	}

	// connect nodes
	if(x < temp->a) temp->left = cur ;
	if(x > temp->a) temp->right = cur;
	if(x == temp->a) printf("error!\n");

	return tree;
}

void preorder(NODE tree)
{
	printf("%d ", tree->a);
	if(tree->left) preorder(tree->left);
	if(tree->right) preorder(tree->right);
}


void inorder(NODE tree)
{
	if(tree->left) inorder(tree->left);
	printf("%d ", tree->a);
	if(tree->right) inorder(tree->right);
}


void postorder(NODE tree)
{
	if(tree->left) postorder(tree->left);
	if(tree->right) postorder(tree->right);
	printf("%d ", tree->a);
}
