#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define SWAP(a,b) { int t;t=a;a=b;b=t; }

void QuickSort(int *ar, int num)
{
     int left,right;
     int key;

     if (num <= 1) return;

     key=ar[num-1];
     for (left=0,right=num-2;;left++,right--) 
	 {
          while (ar[left] < key) 
          	left++;
          while (ar[right] > key) 
          	right--;

          if (left >= right) 
          	break;
          SWAP(ar[left],ar[right]);
     }
     SWAP(ar[left],ar[num-1]);                  
     QuickSort(ar,left); 
     QuickSort(ar+left+1,num-left-1);
}

int binary_search(int list[], int n, int x)
{
	unsigned high,low,mid;
	low=0;
	high=n-1;

	while(1)
	{
		mid=(high+low)/2;

		if (list[mid]==x) 
			break;

		if (list[mid]>x)
			high=mid-1;
		else 
			low=mid+1;

		if (high==low)
			return high;
	}
	return mid;
}


int main()
{
	int a,i;
	int idx,key;
	int *arr;

	printf("input size of array : ");
	scanf("%d",&a);
	arr=(int *)malloc(a*sizeof(int));

	srand(time(NULL));
	for(i=0;i<a;i++)
		arr[i]=rand();

	printf("\ncreated number :\n");
	for(i=0;i<a;i++)
		printf("%d\n",arr[i]);


	QuickSort(arr,a);	//quick sorting

	for(i=0;i<a;i++)
		printf("%d\n",arr[i]);

	printf("\ninput number you want to find : ");
	scanf("%d",&key);

	idx=binary_search(arr,a,key);
	printf("\nthe number is in <%d> position\n",idx+1);
}
