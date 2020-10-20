#include <stdio.h>
#include <stdlib.h>

// Hàm đổi giá trị
void swap(int &a, int &b){
	int tmp = a;
	a       = b;
	b       = tmp;
}

// Vun lại đống tại nút root
void Heapify(int a[], int root, int size){
	int left  = 2 * root + 1;
	int right = 2 * root + 2;
	int key;
	if ((left <= size) && (a[left] > a[root])){
		key = left;
	}
	else{
		key = root;
	}
	if ((right <= size) && (a[right] > a[key])){
		key = right;
	}
	if (key != root){
		swap(a[key], a[root]);
		Heapify(a, key, size);
	}
}

// Vun lại đống từ nút (size/2) đến nút 0 
void CreatHeap(int a[], int len){
	int root;
	int size = len - 1;
	for (root = (size / 2); root >= 0; root --){
		Heapify(a, root, size);
	}
}

// Sắp xếp hoiiiiiiiiiiiiiiiii
void HeapSort(int a[], int len){
	// Vun đống MAX
	CreatHeap(a, len);
	for (int size = len - 1; size >= 0; size --){
		swap(a[0], a[size]);
		Heapify(a, 0, size - 1);
	}
}

//
int main(){
	int len;
    printf("Nhap so luong phan tu = "); scanf("%d", &len);
    int* a = (int*) malloc(len * sizeof(int));
    int i;
    for (i = 0; i < len; i++)
    {
        printf("Nhap PTa[%d]: ",i); scanf("%d", &a[i]);
    }
    HeapSort(a, len);
    for (i = 0; i < len; i++)
    {
        printf("%d  ",a[i]);
    }
    return 0;
}