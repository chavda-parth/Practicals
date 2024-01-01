#include<stdio.h>

void main() {
	int n = 6;
	int numbers[] = {1, 2, 3, 4, 5, 6};
	
	int i, j, temp;
	
	int flag = 0;
	int pass = 0;

	for(i = 0; i < n-1; i++) {
		pass++;
		flag = 0;
		
		for(j = 0; j < n-i-1; j++) {
			if(numbers[j] > numbers[j + 1]) {
				temp = numbers[j];
				numbers[j] = numbers[j + 1];
				numbers[j + 1] = temp;
				flag = 1;
			}
		}
		
		if(flag == 0) {
			break;
		}
	}
	
	printf("%d \n",pass);
	
	for(i = 0; i < n; i++) {
		printf("%d ", numbers[i]);
	}
}
