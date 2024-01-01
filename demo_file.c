#include<stdio.h>

void main() {
	FILE *f = fopen("numberfile.txt", "r");
	FILE *g = fopen("numberfile2.txt","w");
	
	int size = 0;
	int value;
	
	while(fscanf(f, "%d", &value) == 1) {
		printf("%d", value);
		fprintf(g, "%d ", value * 2);
	}
	
	
	
	fclose(f);
	fclose(g);
}
