''' 
Problem of the Day 16 - 25th Sep 2024

Palindrome Linked List

Given a singly linked list of integers. The task is to check if the given linked list is palindrome or not.

Example:

Input: LinkedList: 1->2->1->1->2->1

Output: true

Explanation: The given linked list is 1->2->1->1->2->1 , which is a palindrome and Hence, the output is true.

'''

#Code

class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class Solution:
    def isPalindrome(self, head: Node) -> bool:
        if not head or not head.next:
            return True

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        left, right = head, prev
        while right:
            if left.data != right.data:
                return False
            left = left.next
            right = right.next

        return True

def create_linked_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    return head