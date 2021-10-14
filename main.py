from DataSructures.LinkedList import SinglyLinkedList
from Algorithms.sort import *
from Problems.calculate_expression import calculate_expression

if __name__ == '__main__':
    # arr = [38, 27, 43, 3, 9, 82, 10]
    # heap_sort(arr)
    # print(arr)
    expression = "(5+6*(3+2))*5+3"
    print(calculate_expression(expression))

