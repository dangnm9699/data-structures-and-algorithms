#include <stdio.h>
#include <stdlib.h>

/*
	1. Ta chia đôi dãy thành 2 dãy con, chia cho đến khi dãy con 
	chỉ chứa 1 phần tử.
	2. Ta tiến hành trộn 2 dãy con thành dãy lớn hơn và sắp xếp.
*/
void Merge(int a[], int low, int mid, int high){
	int tmp[high + 1]; // Mảng phụ
	int low1 = low, high1 = mid;
	int low2 = mid + 1, high2 = high;
	int index = 0;
	/* 
		1. Dãy a[low...mid] và dãy a[mid+1...high] đã được sắp xếp
		nên ta sẽ so sánh phần tử nhỏ nhất cả 2 dãy với nhau.
		2. Mỗi khi thu về 1 giá trị MIN, ta sẽ tăng giá trị low của
		dãy chứa MIN cũng như biến chạy index thêm 1 đơn vị.
		3. Khi giá trị 1 trong 2 dãy có giá trị low > high, thoát 
		vòng lặp while.
	*/
	while((low1 <= high1) && (low2 <= high2)){
		if (a[low1] < a[low2]) {
			tmp[index] = a[low1];
			index ++;
			low1  ++;
		}
		else{
			tmp[index] = a[low2];
			index ++;
			low2  ++;
		}
	}
	/*
		1. Khi 1 trong 2 dãy có giá trị low > high, ta sẽ thêm lần 
		lượt đến hết các phần tử ở dãy còn lại vào mảng phụ tmp 
		nếu dãy đó có giá trị low <= high
		2. Cơ chế tương tự như trên, khi 1 phần tử được lấy ra, 
		biến low và biến chạy index sẽ tăng 1 đơn vị.
	*/
	if (low1 > high1){
		while (low2 <= high2){
			tmp[index] = a[low2];
			index ++;
			low2  ++;
		}
	}
	if (low2 > high2){
		while (low1 <= high1){
			tmp[index] = a[low1];
			index ++;
			low1  ++;
		}
	}
	/*
		Sau khi đã sắp xếp xong, ta tiến hành gán giá trị từ 
		mảng phụ vào mảng a ban đầu.
	*/
	int i;
	for (i = low; i <= high; i++){
		a[i] = tmp[i - low];
	}
	return;
}


void MergeSort(int a[], int low, int high){
	// Sắp xếp dãy a[low...high]
	if (low < high) {
		int mid = (low + high) / 2;
		// Sắp xếp dãy a[low...mid]
		MergeSort(a, low, mid);
		// Sắp xếp dãy a[mid+1...high]
		MergeSort(a, mid + 1, high);
		// Trộn 2 dãy đã sắp xếp
		Merge(a, low, mid, high);
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
    MergeSort(a, 0, n - 1);
    for (i = 0; i < n; i++)
    {
        printf("%d  ",a[i]);
    }
    return 0;
}