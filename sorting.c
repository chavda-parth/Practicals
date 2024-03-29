#include<stdio.h>

void selection_sort(int a[], int n) {
	int i, j, minx, minj;
	
	for(i = 0; i < n - 1; i++){
		minj = i;
		minx = a[i];
		
		
		for(j = i + 1; j < n; j++) {
			if(minx > a[j]) {
				minx = a[j];
				minj = j;
			}
		}
		
		if(minj != i) {
			a[minj] = a[i];
			a[i] = minx;
		}
	}
	
	printf("Sorted by selection sort: ");
	
	for(i = 0; i < n; i++) {
		printf("%d ", a[i]);		
	}
}

void insertion_sort(int a[], int n) {
	int i, j, temp;
	
	for(i = 1; i < n; i++) {
		temp = a[i];
		j = i - 1;
		
		while(temp < a[j] && j >= 0) {
			a[j + 1] = a[j];
			j = j - 1;
		}
		
		a[j + 1] = temp;
	}
	
	printf("\nSorted by insertion sort: ");
	
	for(i = 0; i < n; i++) {
		printf("%d ", a[i]);		
	}
	
	printf("\n");
}

void main() {
	int size;
	
	printf("Enter size: ");
	scanf("%d", &size);
	
	int arr[size];
	
	int i;
	
	printf("Enter elements: ");
	
	for(i = 0; i < size; i++) {
		scanf("%d", &arr[i]);
	}
	
	selection_sort(arr, size);
	
	insertion_sort(arr, size);
}



                                                                                                                                                       
