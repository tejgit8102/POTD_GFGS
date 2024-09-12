'''
    Problem of the Day 3 - 12th Sep 2024

    Given the head of a linked list, the task is to find the middle. For example, the middle of 1-> 2->3->4->5 is 3. If there are two middle nodes (even count), return the second middle. For example, middle of 1->2->3->4->5->6 is 4.

    Example:

    Input: Linked list: 1->2->3->4->5
    Output: 3

    Explanation: The given linked list is 1->2->3->4->5 and its middle is 3.
'''

#Code

class Solution:
    def getMiddle(self, head):
        if not head:
            return -1
        
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow.data