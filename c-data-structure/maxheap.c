#include <stdio.h>
#include <stdlib.h>
#define SWAP(a,b) ((a)^=(b)^=(a)^=(b))

void BuildMaxHeap(int heap[], int array_size);
void MaxHeapify(int heap[], int i, int array_size);
int ExtractMax(int heap[], int array_size);

int main()
{
	int N, k;
	int i;
	int *heap;

	while(1){
		scanf("%d %d", &N, &k);
		if( (N>=1) && (N<=100000) && (k>=1) && (k<=30) ) break;
	}

	heap = (int *)malloc(sizeof(int)*(N+1));
	heap[0] = 0;

	for(i=1; i<=N; i++)
		scanf("%d", &heap[i]);

	BuildMaxHeap(heap, N);

	for(i=N; i>N-k; i--)
		printf("%d ", ExtractMax(heap, i));
	printf("\n");

	for(i=1; i<=N-k; i++)
		printf("%d ", heap[i]);

	return 0;
}


void MaxHeapify(int heap[], int i, int array_size)
{
	int left = 2*i;
	int right= 2*i+1;
	int big;

	if( (left<=array_size) && (heap[left]>heap[i]) )
		big = left;
	else
		big = i;

	if( (right<=array_size) && (heap[right]>heap[big]) )
		big = right;

	if(big != i){
		SWAP(heap[i], heap[big]);
		MaxHeapify(heap, big, array_size);
	}
	return;
}

void BuildMaxHeap(int heap[], int array_size)
{
	int i = array_size / 2;
	for(; i>=1; i--)
		MaxHeapify(heap, i, array_size);
	return;
}

int ExtractMax(int heap[], int array_size)
{
	int max;
	if(array_size < 1) return -1;

	max = heap[1];
	heap[1] = heap[array_size];

	array_size = array_size - 1;
	BuildMaxHeap(heap, array_size);

	return max;
}
