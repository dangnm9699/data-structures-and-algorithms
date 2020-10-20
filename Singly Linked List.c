#include <stdlib.h>
#include <stdio.h>
#include <conio.h>

struct Node {
	int data;
	struct Node* next;
};
typedef struct Node NODE;

NODE* Taonode(int val) {
	NODE* tmp;
	tmp = (NODE*)malloc(sizeof(NODE));
	tmp->data = val;
	tmp->next = NULL;
	return tmp;
}

NODE* Themdau(NODE* first, int val) {
	NODE* tmp = Taonode(val);
	if (first == NULL) {
		first = tmp;
	}
	else {
		tmp->next = first;
		first = tmp;
	}
	return first;
}

NODE* Themduoi(NODE* first, int val) {
	NODE* tmp = Taonode(val);
	NODE* p;
	if (first == NULL)
		first = tmp;
	else {
		p = first;
		while (p->next != NULL)
			p = p->next;
		p->next = tmp;
	}
	return first;
}

NODE* Thembatky(NODE* first, int val, int pos) {
	printf("\n   => THEM NODE TAI VI TRI %d CUA DANH SACH!\n",pos);
	if (pos == 1 || first == NULL) {
		first = Themdau(first, val);
		printf(":::   DONE!");
	}
	else {
		int k = 2;
		NODE* p = first;
		while (p != NULL && k != pos) {
			p = p->next;
			k++;
		}// ra khoi vong lap while ta co gia tri k. bay gio ta so sanh k voi bien vi tri;
		if (k != pos) {
			printf(":::   Vi tri can them nam ngoai danh sach nen ta them node tai cuoi danh sach!");
			first = Themduoi(first, val);
		}
		else {
			// 
			NODE* tmp = Taonode(val);
			tmp->next = p->next;
			p->next = tmp;
		}
	}
	return first;
}

void Inds(NODE* first) {
	printf("\n   => IN DANH SACH RA MAN HINH! \n");
	printf(":::");
	for (NODE* p = first; p != NULL; p = p->next) {
		printf("%5d", p->data);
	}
}

NODE* khoitao() {
	NODE* first;
	first = NULL;
	return first;
}

NODE* Xoadau(NODE* first) {
	printf("\n   => XOA NODE DAU TIEN CUA DANH SACH!\n");
	if (first == NULL) {
		printf(":::   Khong co gi de xoa ca!");
		return NULL;
	}
	else {
		if (first->next == NULL) {
			printf(":::   Danh sach da xoa 1 phan tu thanh danh sach rong!");
			return NULL;
		}
		else {
			NODE* p = first;
			first = first->next;
			delete p;
			printf(":::   DONE!");
			return first;
		}
	}
}

NODE* Xoaduoi(NODE* first) {
	printf("\n   => XOA NODE CUOI CUNG CUA DANH SACH!\n");
	if (first == NULL) {
		printf(":::   Khong co gi de xoa ca!");
		return NULL;
	}
	else {
		if (first->next == NULL) {
			printf(":::   Danh sach da xoa 1 node thanh danh sach rong!");
			return NULL;
		}
		else {
			NODE* p = first;
			while (p->next->next != NULL) {
				p = p->next;
			}
			NODE* q = p->next;
			p->next = NULL;
			delete q;
			printf(":::   DONE!");
			return first;
		}
	}
}

NODE* Xoabatky(NODE* first, int pos) {
	printf("\n   => XOA NODE THU %d CUA DANH SACH!\n",pos);
	NODE* p = first;
	NODE* prev = NULL;
	int k = 1;
	if (first == NULL) {
		printf(":::   Khong co gi de xoa ca!");
		return NULL;
	}
	if (first->next == NULL) {
		first = Xoadau(first);
		return first;
	}
	while (p != NULL && k != pos) {
		prev = p;
		p = p->next;
		k++;
	}
	//thoat khoi vong lap, ta co 1 gia tri k.
	if (k != pos) {
		printf(":::   Vi tri xoa nam ngoai danh sach nen khong xoa!");
		return first;
	}
	else {
		NODE* q = p;
		prev->next = p->next;
		delete q;
		printf(":::   DONE!");
		return first;
	}
}

NODE* Daods(NODE* first) {
	NODE* curr = NULL;
	NODE* prev = NULL;
	printf("\n   => DAO DANH SACH!\n");
	if (first == NULL) {
		printf(":::   Danh sach rong, khong the dao!");
		return NULL;
	}
	NODE* p = first;
	while (p != NULL) {
		curr = p;
		p = p->next;
		curr->next = prev;
		prev = curr;
	}
	first = curr;
	printf(":::   DONE!");
	return first;
}

NODE* Nhapds() {
	NODE* first = khoitao();
	int n, x;
	do {
		printf("Nhap so luong node: ");
		scanf("%d", &n);
	} while (n <= 0);
	for (int i = 0; i < n; i++) {
		printf("\nNhap gia tri nut %d: ", i + 1);
		scanf("%d", &x);
		first = Themduoi(first, x);
	}
	return first;
}

int main() {
	NODE* first;
	first = Nhapds();
	Inds(first);
	first = Xoadau(first);
	Inds(first);
	first = Xoaduoi(first);
	Inds(first);
	first = Thembatky(first, 90, 1);
	Inds(first);
	first = Xoabatky(first, 2);
	Inds(first);
	first = Daods(first);
	Inds(first);
}

