#include<stdio.h>
#include<stdlib.h>
#include<math.h>

void main() {
	FILE *f1 = fopen("bestCase500.txt", "w");
	FILE *f2 = fopen("worstCase500.txt", "w");
	FILE *f3 = fopen("averageCase500.txt", "w");
	
	int i;
	
	for(i = 1; i <= 500; i++) {
		fprintf(f1, "%d\n", i);
		fprintf(f2, "%d\n", 501 - i);
		fprintf(f3, "%d\n", rand() % 500);
	}
	
	fclose(f1);
	fclose(f2);
	fclose(f3);
}
