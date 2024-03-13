# C Program Practice
## Factorial
```c
# include <stdio.h>
int facto(int c)
{
    if (c==0)
    return 1;
    else
        return (int)c * facto(c-1);
}



int main()
{
    int c,fact;
    scanf("%d",&c);
    fact=facto(c);
    printf("%d",fact);
    return 0;
}

```
## Understand Pointer
```c
#include <stdio.h>
int j, k;
int *ptr;
int main(void)
{
j = 1;
k = 2;
ptr = &k;
printf("\n");

printf("j has the value %d and is stored at %p\n", j, (void *)&j);
printf("k has the value %d and is stored at %p\n", k, (void *)&k);
printf("ptr has the value %p and is stored at %p\n", ptr, (void
*)&ptr);
printf("The value of the integer pointed to by ptr is %d\n", *ptr);
return 0;
}
```

## Understand Array And Pointer
```c
# include <stdio.h>
#include <stdio.h>
int my_array[] = {1,23,17,4,-5,100};
int *ptr;
int main(void)
{
int i;
ptr = &my_array[0];
if (ptr == my_array) printf("%d",ptr);
printf("\n\n");
for (i = 0; i < 6; i++)
{
printf("my_array[%d] = %d ",i,my_array[i]); 
printf("ptr + %d = %d\n",i, *(ptr + i));
return 0;
}

```

## Adding New Node In The Starting Of Linked List
```c
#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    struct node *lp;
    int data;
    struct node *rp;
} sn;

void view (sn *node) {
    if (node == NULL) {
        return;
    }
    else {
        while (node->rp != NULL) {
            printf("%d ",node->data);
            node = node->rp;
            }
        printf("%d",node->data);
    }
}

sn *addnode(sn *node) {
    sn *new1 = (sn *)malloc(sizeof(sn));
    new1->lp = NULL;
    new1->rp = node;
    int n;
    printf("\nEnter the value for new node: ");
    scanf("%d",&n);
    new1->data = n;
    node->lp = new1;
    return new1;
}
int main() {
    
    sn *one;
    sn *two;
    sn *three;
    sn *four;
    
    one = (sn *)malloc(sizeof(sn));
    two = (sn *)malloc(sizeof(sn));
    three = (sn *)malloc(sizeof(sn));
    four = (sn *)malloc(sizeof(sn));
    
    one->lp = NULL;
    one->data = 1;
    one->rp = two;
    
    two->lp = one;
    two->data = 2;
    two->rp = three;
    
    three->lp = two;
    three->data = 3;
    three->rp = four;
    
    four->lp = three;
    four->data = 4;
    four->rp = NULL;
    
    view(one);
    sn *root=addnode(one);
    view(root);
    
    free(one);
    one = NULL;
    
    free(two);
    two = NULL;
    
    free(three);
    three = NULL;
    
    free(four);
    four = NULL;
    
    
    return 0;
}

```

## Adding New Node In The End Of Linked List
```c
#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *next;
};

void view(struct node *head) {
    while (head != NULL) {
        printf("%d\n",head -> data);
        head = head -> next;
    }
}

void add(struct node *head, struct node *add) {
    while (head->next != NULL) {
        head = head -> next;
    }
    head -> next = add;
}

int main() {
    
    struct node head;
    struct node *a;
    struct node *b;
    struct node *c;
    struct node *d;
    struct node *e;

    a=(struct node* )malloc(sizeof(struct node));
    b=(struct node* )malloc(sizeof(struct node));
    c=(struct node* )malloc(sizeof(struct node));
    d=(struct node* )malloc(sizeof(struct node));
    e=(struct node* )malloc(sizeof(struct node));

    head.data = 0;
    head.next = a;

    a -> data = 1;
    a -> next = b;

    b -> data = 2;
    b -> next = c;

    c -> data = 3;
    c -> next = d;

    d -> data = 4;
    d -> next = NULL;
    
    e -> data = 5;
    e -> next = NULL;
    
    printf("Before adding: \n");
    view(head.next);
    add(head.next,e);
    printf("After adding node: \n");
    view(head.next);

    free(a);
    free(b);
    free(c);
    free(d);
    free(e);

    a = NULL;
    b = NULL;
    c = NULL;
    d = NULL;
    e = NULL;

    return 0;
}
```

## Adding New Node In The Between Of Linked List
```c
#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *next;
};

void view(struct node *head) {
    while (head != NULL) {
        printf("%d\n",head -> data);
        head = head -> next;
    }
}

void add(struct node *find,struct node *head, struct node *add) {
    while (head != NULL && head != find) {
        head = head -> next;
    }
    add -> next = head -> next;
    head -> next = add;
}

int main() {
    
    struct node head;
    struct node *a;
    struct node *b;
    struct node *c;
    struct node *d;
    struct node *e;

    a=(struct node* )malloc(sizeof(struct node));
    b=(struct node* )malloc(sizeof(struct node));
    c=(struct node* )malloc(sizeof(struct node));
    d=(struct node* )malloc(sizeof(struct node));
    e=(struct node* )malloc(sizeof(struct node));

    head.data = 0;
    head.next = a;

    a -> data = 1;
    a -> next = b;

    b -> data = 2;
    b -> next = c;

    c -> data = 3;
    c -> next = d;

    d -> data = 4;
    d -> next = NULL;
    
    e -> data = 5;
    e -> next = NULL;
    
    printf("Before adding: \n");
    view(head.next);
    add(d,head.next,e);
    printf("After adding node: \n");
    view(head.next);

    free(a);
    free(b);
    free(c);
    free(d);
    free(e);

    a = NULL;
    b = NULL;
    c = NULL;
    d = NULL;
    e = NULL;

    return 0;
}
```

## Deleting Node From Linked List
```c
#include <stdio.h>
#include <stdlib.h>

struct node { // creating manual data type
    int data;
    struct node *next;
};

void view(struct node *head) { // defining a function "view"
    while (head != NULL) { // until head is null it will print the data in node
        printf("%d ",head -> data);
        head = head -> next;
    }
    printf("\n");
}
void del(struct node *f,struct node h,struct node *head) { 
    if (head == f) { // if we want to delete the first node
        h.next=f->next;
        return;
    }
    while (head->next !=NULL && head->next !=f) {
        head = head->next;
    }
    // if given node is not present 
    if (head->next == NULL) {
        return;
    }
    head->next=f->next;
}
int main() {
    
    // declaring the nodes
    struct node head; 
    struct node *a;
    struct node *b;
    struct node *c;
    struct node *d;
    
    // allocating the memory
    a = (struct node*)malloc(sizeof(struct node)); 
    b = (struct node*)malloc(sizeof(struct node));
    c = (struct node*)malloc(sizeof(struct node));
    d = (struct node*)malloc(sizeof(struct node));
    
    // initialisation 
    head.data = 0;
    head.next = a;
    
    a->data = 1;
    a->next = b;
    
    b->data = 2;
    b->next = c;
    
    c->data = 3;
    c->next = d;
    
    d->data = 4;
    d->next = NULL;
    
    view (head.next); // calling the funtions
    
    del (d,head,&head);
    
    
    view (head.next);
    
    free(a); // making the pointers free
    a = NULL; // avoiding dangling pointers
    
    free(b);
    b = NULL;
    
    free(c);
    c = NULL;
    
    free(d);
    d = NULL;
    
    return 0;
}
```

## Double Linked List
```c

#include <stdio.h>
#include <stdlib.h>

typedef struct node {

	int val;
	struct node* next;
	struct node * prev;

}bTree;

struct node * head = NULL; //head : first node.
const int sizeof_node = sizeof(bTree);

bTree* createNode(int val){
	bTree *node = (bTree *)malloc(sizeof_node);

	node->val = val;

	node->next = NULL;
	node->prev = NULL;

	return node;
}
int insertNodeAtEnd(int val){
	
	bTree *node = createNode(val);

	if (head == NULL){
		head = node;
	}
	else{
		bTree *ptr = head;

		while(ptr->next != NULL){
			ptr = ptr->next;
		}
		bTree *prev = ptr;
		ptr->next = node; //ptr is currently at the last element, it's next points to the NULL, inplace of NULL we set the new element


		node->prev = prev;
	}

}
int getLength(bTree *head1){

    if(head1 == NULL){
        return 0;
    }
    else{
        return 1 + getLength(head1->next); // head1->next becomes the new head1.
    }
}

int printAllNodes(){

	if (head == NULL){
		return -1;
	}
	else{
		bTree * ptr = head; 

		while( ptr->next != NULL){
			printf("%d ",ptr->val);
			ptr = ptr->next;
		}
		printf("%d\n", ptr->val); //printing the last node
	}

}

int deleteNodeAt(int position){

	if (position > getLength(head)){
		printf("what are u doing?");
		return 0;
	}
	int i;
	bTree *prev = NULL;
	bTree *cur = head;
	bTree *next = NULL;

	for(i = 1;i<position;i++){

		next = cur->next;
		prev = cur;

		cur = cur->next;

		//cur now at the node that is to be deleted.

	}
	/*ex: pos = 5;
		first iteration -> cur = 2nd
		second iterat -> cur = 3rd
		third iterat -> cur = 4th
		fourth -> cur = 5th (actual position) & prev = 4th

		nodeToBeDel = 5th pos.
		next node = 6th's prev is set to 4th node 

	*/

	bTree * nodeToBeDel = cur;
	prev->next = cur->next;
	(cur->next)->prev = prev;

	free(nodeToBeDel);
	nodeToBeDel = NULL;
}

int insertAtPos(int pos, int val){
	if(pos > getLength(head)){
		insertNodeAtEnd(val);
	}
	else
	{
		int i;
		bTree *prev = NULL;
		bTree *cur = head;
		bTree *next = NULL;

		for(i=1;i<pos;i++)
		{
			next = cur->next;
			prev = cur;

			cur = cur->next; // at the end we'll reach the position where we want to insert the element

		}
		bTree *newNode = createNode(val);
		prev->next = newNode;
		cur->prev = newNode;

		newNode->next = cur;
		newNode->prev = prev;

	}
}

int main(){

	int i;
	int len = 125;

	for(i = 1;i<=len;i++){
		insertNodeAtEnd(i);
	}

	printAllNodes();
	printf("\nLength of the list:  %d\n",getLength(head));

	deleteNodeAt(10);
	printAllNodes();

	insertAtPos(10,200);
	insertAtPos(10,10);
	
	printf("\n");
	printAllNodes();

	printf("\nLength of the list:  %d\n",getLength(head));



	return 0;
}
```