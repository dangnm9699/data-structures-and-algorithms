#include <stdio.h>
#include <stdlib.h>

/*
	
*/

// Đổi giá trị 2 vị trí
void swap(int &a, int &b){
	int tmp = a;
	a       = b;
	b		= tmp;
}

// Chọn phần tử đầu làm Pivot
int PartitionL(int a[], int left, int right){
	int pivot = a[left];
	int i = left + 1, j = right;
	while (true){
		// Tìm phần tử >= Pivot
		while ((i <= right) && (a[i]) < pivot) i ++;
		// Tìm phần tử <= Pivot
		while ((j >= left)  && (a[j]) > pivot) j --;
		// Khi biến tăng >= biến lùi thì thoát vòng lặp
		if(i >= j)
			break;
		// Swap 2 giá trị vừa tìm được bên trên
		swap(a[i], a[j]);
		// Tăng biến tăng, giảm biến lùi để xét các phần tử tiếp theo
		i ++;
		j --;
	}
	// Swap để đưa giá trị Pivot vào giữa
	swap(a[j], a[left]);
	// Trả về vị trí của Pivot
	return j;
}

// Chọn phần tử cuối làm Pivot
int PartitionR(int a[], int left, int right){
	int pivot = a[right];
	int i = left, j = right - 1;
	while (true){
		// Tìm phần tử >= Pivot
		while ((i <= right) && (a[i] < pivot)) i ++;
		// Tìm phần tử <= Pivot
		while ((j >= left)  && (a[j] > pivot)) j --;
		// Khi biến tăng >= biến lùi thì thoát vòng lặp
		if(i >= j)
			break;
		// Swap 2 giá trị vừa tìm được bên trên
		swap(a[i], a[j]);
		// Tăng biến tăng, giảm biến lùi để xét các phần tử tiếp theo
		i ++;
		j --;
	}
	// Swap để đưa giá trị Pivot vào giữa
	swap(a[right], a[i]);
	// Trả về vị trí của Pivot
	return i;
}

//
void QuickSort(int a[], int left, int right){
	if (left < right){
		//
		int pivot = PartitionR(a, left, right);
		//
		QuickSort(a, left, pivot - 1);
		//
		QuickSort(a, pivot + 1, right);
	}
}

//
int main(){	
	int n;
    printf("Nhap so luong phan tu n = "); scanf("%d", &n);
    int* a = (int*) malloc(n * sizeof(int));
    int i;
    for (i = 0; i < n; i++)
    {
        printf("Nhap PTa[%d]: ",i); scanf("%d", &a[i]);
    }
    QuickSort(a, 0, n - 1);
    for (i = 0; i < n; i++)
    {
        printf("%d  ",a[i]);
    }
    return 0;
}