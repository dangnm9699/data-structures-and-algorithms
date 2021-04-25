class Data:
    def __init__(self, id, name):
        self.id = id
        self.name = name


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
        pass

    def remove_tail(self):
        pass

    def print_list(self):
        curr = self.head
        print('Head')
        while (curr):
            print(
                '-> [id = {} name = {}]'.format(curr.data.id, curr.data.name))
            curr = curr.next
        print('-> Tail')


if __name__ == '__main__':
    sll = SinglyLinkedList()
    sll.add_head(Data(1, 'dangnm'))
    sll.add_head(Data(2, 'dongnt'))
    sll.add_head(Data(3, 'quanvd'))

    sll.print_list()
