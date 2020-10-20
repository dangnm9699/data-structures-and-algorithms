#include <stdio.h> 
#include <stdlib.h>
/*
	
*/
void BubbleSort(int a[], int n){
	int i, j;
	for (i = 0; i < n - 1; i++){
		for (j = 0; j < n - 1 - i; j++){
			if (a[j] > a[j+1]){
				int tmp;
				tmp = a[j];
				a[j] = a[j+1];
				a[j+1] = tmp;
			}
		}
	}
}
int main()
{
	int n;
    printf("Nhap so luong phan tu n = "); scanf("%d", &n);
    int* a = (int*) malloc(n * sizeof(int));
    int i;
    for (i = 0; i < n; i++)
    {
        printf("Nhap PTa[%d]: ",i); scanf("%d", &a[i]);
    }
    BubbleSort(a, n);
    for (i = 0; i < n; i++)
    {
        printf("%d  ",a[i]);
    }
    return 0;
}