from typing import List


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self, list: List[any] = None, head=True):
        self.length = 0
        self.head = None
        if list != None and len(list) > 0:
            if head:
                for e in list:
                    self._add_head(e)
            else:
                for e in list:
                    self._add_tail(e)

    def append(self, data=None, head=True):
        if head:
            self._add_head(data)
        else:
            self._add_tail(data)

    def remove_head(self):
        if self.length == 0:
            raise AssertionError("Cannot remove from empty list")
        if self.length == 1:
            self.head = None
            self.length -= 1
        else:
            self.head = self.head.next
            self.length -= 1

    def remove_tail(self):
        if self.length == 0:
            raise AssertionError("Cannot remove from empty list")
        if self.length == 1:
            self.head = None
            self.length -= 1
        else:
            curr = self.head
            while(curr.next.next):
                curr = curr.next
            curr.next = None
            self.length -= 1

    def reverse(self):
        if self.length == 0:
            raise AssertionError("Cannot reverse empty list")
        if self.length == 1:
            return 
        curr = self.head
        prev = None
        next = None
        while(curr):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    def _add_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def _add_tail(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            curr = self.head
            while (curr.next):
                curr = curr.next
            curr.next = Node(data)
        self.length += 1

    def print(self):
        curr = self.head
        print('Head', end='')
        while (curr):
            print(
                '-> [ {} ]'.format(curr.data), end='')
            curr = curr.next
        print('-> Tail')
