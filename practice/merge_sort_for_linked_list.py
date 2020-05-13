"""
from: https://www.geeksforgeeks.org/merge-sort-for-linked-list/
Python3 program to merge sort of linked list
"""


# create Node using class Node.
class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node = None


class LinkedList:
    def __init__(self):
        self.head = None

    # push new value to linked list
    # using append method
    def append(self, new_value):
        # Allocate new node
        new_node = Node(new_value)

        # if head is None, initialize it to new node
        if not self.head:
            self.head = new_node
            return

        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next

        # Append the new node at the end of the linked list
        curr_node.next = new_node

    def sortedMerge(self, a: Node, b: Node):

        # Base cases:
        if not a:
            return b
        if not b:
            return a

        # pick either a or b and recur...
        if a.data <= b.data:
            result = a
            result.next = self.sortedMerge(a.next, b)
        else:
            result = b
            result.next = self.sortedMerge(a, b.next)

        return result

    def mergeSort(self, h: Node):
        # Base case if head is None
        if not h or not h.next:
            return h

        # get the middle of the list
        middle = self.getMiddle(h)
        next_to_middle = middle.next

        # set the next of middle node to None
        middle.next = None

        # Apply mergeSort on left list
        left = self.mergeSort(h)

        # Apply mergeSort on right list
        right = self.mergeSort(next_to_middle)

        # Merge the left and right lists
        sorted_list = self.sortedMerge(left, right)
        return sorted_list

    def getMiddle(self, head: Node):
        if not head:
            return head

        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow


# Utility function to print the linked list
def printList(head: Node):
    if not head:
        print(' ')
        return

    curr_node = head
    while curr_node:
        print(curr_node.data, end=' ')
        curr_node = curr_node.next

    print(' ')


# Driver Code
if __name__ == '__main__':
    li = LinkedList()

    """
    Let us create a unsorted linked list
    to test the functions created.
    The list shall be a: 2->3->20->5->10->15
    """
    li.append(15)
    li.append(10)
    li.append(5)
    li.append(20)
    li.append(3)
    li.append(2)

    # Apply merge sort
    li.head = li.mergeSort(li.head)
    print('Sorted Linked List is: ')
    printList(li.head)

"""
Sorted Linked List is: 
2 3 5 10 15 20  
"""
