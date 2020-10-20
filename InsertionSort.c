#include <stdio.h>
#include <stdlib.h>
/*
    Giả sử đã có dãy k phần tử sắp xếp đúng thứ tự. Bây giờ ta có thêm phần tử thứ (k+1) cần chèn vào dãy và sắp xếp.
    Ta sẽ so sánh phần tử đó với phần tử cuối cùng. Nếu lớn hơn phần tử cuối cùng thì nó đã ở đúng vị trí, còn nếu 
    ngược lại, ta sẽ so sánh lần lượt với các phần tử tiếp theo cho đến đầu danh sách đến khi đúng vị trí.
    
*/
void InsertionSort(int a[], int n){
    int i, j, key;
    for (i = 1; i < n; i++){
        key = a[i];
        j = i;
        while((j > 0) && (a[j-1] > key)){
            a[j] = a[j-1];
            j--;
            a[j] = key;
        }
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
    InsertionSort(a, n);
    for (i = 0; i < n; i++)
    {
        printf("%d  ",a[i]);
    }
    return 0;
}