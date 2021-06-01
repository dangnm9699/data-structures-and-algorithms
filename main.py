from DataSructures.LinkedList import SinglyLinkedList


if __name__ == '__main__':
    list = [1,2,None]
    sll = SinglyLinkedList(list, head=False)
    sll.remove_tail()
    sll.remove_tail()
    sll.remove_tail()
    sll.print()