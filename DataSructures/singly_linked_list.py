class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_tail(self, data):
        new_node = Node(data)
        curr = self.head
        while (curr.next):
            curr = curr.next
        curr.next = new_node

    def remove_head(self):
        self.head = self.head.next

    def remove_tail(self):
        curr = self.head
        while(curr.next.next):
            curr = curr.next
        curr.next = None

    def reverse(self):
        curr = self.head
        prev = None
        next = None
        while(curr):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    def findPreMid(self, head):
        slow = head
        fast = head
        preslow = head
        while(slow and fast):
            preslow = slow
            slow = slow.next
            if fast.next != None:
                fast = fast.next.next
            else:
                fast = fast.next
        return preslow

    def megre(self, head1, head2):
        curr1 = head1
        curr2 = head2

        currRes = res
        while(curr1 and curr2):
            if curr1.data < curr2.data:
                currRes.next = curr1
                currRes = curr1
                curr1 = curr1.next
            else:
                currRes.next = curr2
                currRes = curr2
                curr2 = curr2.next
        while(curr1):
            currRes.next = curr1
            currRes = curr1
            curr1 = curr1.next
        while(curr2):
            currRes.next = curr2
            currRes = curr2
            curr2 = curr2.next
        return res

    def megreSort(self, head):
        if not head.next or not head.next.next:
            return head
        premid = self.findPreMid(head)
        head2 = premid.next
        premid.next = None
        a = self.megreSort(head)
        b = self.megreSort(head2)
        return self.megre(a, b)

    def sort(self):
        self.head = self.megreSort(self.head)

    def print_list(self):
        curr = self.head
        print('Head', end='')
        while (curr):
            print(
                '-> [ {} ]'.format(curr.data), end='')
            curr = curr.next
        print('-> Tail')


if __name__ == '__main__':
    sll = SinglyLinkedList()
    sll.add_head(1)
    sll.add_head(2)
    sll.add_head(3)
    sll.sort()

    sll.print_list()
