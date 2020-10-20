#include <stdio.h>
#include <stdlib.h>
/*
	Chọn vị trí k = 0 là min, duyệt (k+1) đến cuối để tìm vị trí có giá trị nhó hơn.
	Khi tìm được vị trí có giá trị nhỏ nhất, ta đổi giá trị vị trí k và vị trí đó.
	Ta tăng k và tiếp tục làm như vậy
*/
void swap(int &a, int &b){
	int tmp = a;
	a       = b;
	b		= tmp;
}

void SelectionSort(int a[], int n){
	int i, j, min;
	for (i = 0; i < n - 1; i++){
		min = i;
		for (j = i + 1; j < n; j++){
			if (a[j] < a[min])
				min = j;
		}
		swap(a[i], a[min]);
	}
}
int main(){
	int n;
    printf("Nhap so luong phan tu n = "); scanf("%d", &n);
    int* a = (int*) malloc(n * sizeof(int));
    int i;
    for (i = 0; i < n; i++)
    {
        printf("Nhap PTa[%d]: ",i); scanf("%d", &a[i]);
    }
    SelectionSort(a, n);
    for (i = 0; i < n; i++)
    {
        printf("%d  ",a[i]);
    }
    return 0;
}