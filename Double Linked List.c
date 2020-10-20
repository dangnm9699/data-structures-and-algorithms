#include <stdio.h>
#include <stdlib.h>

struct dllist{
	int data;
	dllist* next;
	dllist* prev;
};

typedef struct dllist dnode;

dnode* khoitao(){
	dnode* head;
	head = NULL;
	return head;
}

dnode* taonode(int x){
	dnode* p = (dnode*) malloc(sizeof(dnode));
	p->data = x;
	p->next = NULL;
	p->prev = NULL;
	return p;
}

dnode* themdau(dnode* head, int x){
	dnode* p = taonode(x);
	if (head == NULL){
		head = p;
		return head;
	}
	else{
		p->next = head;
		head->prev = p;
		head = p;
		return head;
	}
}

dnode* themduoi(dnode* head, int x){
	dnode* p = taonode(x);
	dnode* q = head;
	if(head == NULL){
		head = p;
		return head;
	}
	while(q->next != NULL)
		q = q->next;
	q->next = p;
	p->prev = q;
	return head;
}

dnode* xoadau(dnode* head) {
	printf("\n   => XOA PHAN TU DAU TIEN CUA DANH SACH!\n");
	if (head == NULL) {
		printf(":::   Khong co gi de xoa ca!");
		return NULL;
	}
	else {
		if (head->next == NULL) {
			printf(":::   Danh sach da xoa 1 phan tu thanh danh sach rong!");
			return NULL;
		}
		else {
			dnode* p = head;
			head = head->next;
			delete p;
			printf(":::   Hoan tat!");
			return head;
		}
	}
}

dnode* xoaduoi(dnode* head){
	printf("\n   => XOA PHAN TU CUOI CUNG CUA DANH SACH!\n");
	if (head == NULL){
		printf(":::   Khong co gi de xoa!\n");
		return NULL;
	}
	if (head->next == NULL){
		printf(":::   Danh sach da xoa 1 phan tu thanh danh sach rong!");
		return NULL;
	}
	else{
		dnode* p = head;
		while(p->next->next != NULL) // Để lưu p là phần tử ngay sát phần tử cuối
			p = p->next;
		dnode* q = p->next;
		p->next = NULL;
		delete q;
		printf(":::   Hoan tat!");
		return head;
	}
}

dnode* Xoabatky(dnode* head, int pos) {
	printf("\n   => XOA PHAN TU THU %d CUA DANH SACH!\n",pos);
	dnode* p = head;
	int k = 1;
	if (head == NULL) {
		printf(":::   Khong co gi de xoa ca!");
		return NULL;
	}
	if (head->next == NULL) {
		head = xoadau(head);
		return head;
	}
	while (p != NULL && k != pos) {
		p = p->next;
		k++;
	}
	//thoat khoi vong lap, ta co 1 gia tri k.
	if (k != pos) {
		printf(":::   Vi tri xoa nam ngoai danh sach nen khong xoa!");
		return head;
	}
	else {
		dnode* q = p;
		dnode* nex = p->next;
		dnode* pre = p->prev;
		if (nex == NULL){
			pre->next = NULL;
			delete q;
			return head;
		}
		pre->next = nex;
		nex->prev = pre;
		delete q;
		printf(":::   Hoan tat!");
		return head;
	}
}

dnode* nhapds() {
	dnode* head = khoitao();
	int n, x;
	do {
		printf(":::   Nhap so luong node: ");
		scanf("%d", &n);
	} while (n <= 0);
	for (int i = 0; i < n; i++) {
		printf("\n:::   . Nhap gia tri nut %d: ", i + 1);
		scanf("%d", &x);
		head = themduoi(head, x); 
		// Co the thay bang themduoi(head, x)
	}
	return head;
}

void inds(dnode* head) {
	printf("\n   => IN DANH SACH RA MAN HINH! \n");
	printf(":::");
	for (dnode* p = head; p != NULL; p = p->next) {
		printf("%4d", p->data);
	}
}

int main(){
	dnode* head;
	head = nhapds();
	inds(head);
	head = xoadau(head);
	inds(head);
	head = xoaduoi(head);
	inds(head);
	head = Xoabatky(head, 3);
	inds(head);
	return 0;
}